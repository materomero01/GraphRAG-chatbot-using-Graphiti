import asyncio
import os
from datetime import datetime, timezone
from typing import List, Any, Optional
from dotenv import load_dotenv

# Graphiti
from graphiti_core import Graphiti
from graphiti_core.llm_client.gemini_client import GeminiClient, LLMConfig
from graphiti_core.embedder.gemini import GeminiEmbedder, GeminiEmbedderConfig
from graphiti_core.cross_encoder.gemini_reranker_client import GeminiRerankerClient

# LangChain
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.tools import tool

# Modelo LLM GEMINI
from langchain_google_genai import ChatGoogleGenerativeAI

# ==================== CONFIG ====================
load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

graphiti: Graphiti = None

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.3,
)

# ==================== GRAPHITI ====================
async def get_graphiti() -> Graphiti:
    global graphiti
    if graphiti is None:
        print("Inicializando Graphiti...")
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY no configurada")

        llm_client = GeminiClient(LLMConfig(api_key=GEMINI_API_KEY, model="gemini-2.5-flash"))
        embedder = GeminiEmbedder(GeminiEmbedderConfig(api_key=GEMINI_API_KEY, embedding_model="text-embedding-004"))
        reranker = GeminiRerankerClient(LLMConfig(api_key=GEMINI_API_KEY, model="gemini-2.5-flash"))

        graphiti = Graphiti(
            NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD,
            llm_client=llm_client,
            embedder=embedder,
            cross_encoder=reranker
        )
        print("Graphiti listo")
    return graphiti


# ==================== TOOLS (ARREGLADAS) ====================
@tool
async def search_hybrid(query: str) -> str:
    """Búsqueda híbrida general en Graphiti. Proporciona hasta 5 resultados relevantes."""
    g = await get_graphiti()
    results = await g.search(query=query, num_results=5)
    if not results:
        return "No se encontraron resultados relevantes."
    return "\n".join([f"- {r.fact if hasattr(r, 'fact') else getattr(r, 'name', 'Sin nombre')}" for r in results])


@tool
async def search_temporal(query: str, date: str) -> str:
    """Búsqueda con fecha (YYYY-MM-DD). Filtra hechos válidos en esa fecha."""
    try:
        ref_time = datetime.fromisoformat(date.replace('Z', '+00:00'))
        if ref_time.tzinfo is None:
            ref_time = ref_time.replace(tzinfo=timezone.utc)
        ref_time = ref_time.astimezone(timezone.utc)
    except ValueError:
        return "Fecha inválida. Usa YYYY-MM-DD (ej: 2024-03-01)."

    g = await get_graphiti()
    results = await g.search(query=query, num_results=10)

    filtered = []
    for r in results:
        if hasattr(r, 'fact'):
            valid_at = getattr(r, 'valid_at', None)
            invalid_at = getattr(r, 'invalid_at', None)

            # NORMALIZAR TIMEZONES
            if valid_at:
                if valid_at.tzinfo is None:
                    valid_at = valid_at.replace(tzinfo=timezone.utc)
                valid_at = valid_at.astimezone(timezone.utc)

            if invalid_at:
                if invalid_at.tzinfo is None:
                    invalid_at = invalid_at.replace(tzinfo=timezone.utc)
                invalid_at = invalid_at.astimezone(timezone.utc)

            # FILTRAR POR VALIDEZ
            if (not valid_at or valid_at <= ref_time) and (not invalid_at or invalid_at > ref_time):
                filtered.append(r)
        else:
            filtered.append(r)

    filtered = filtered[:5]
    if not filtered:
        return f"No hay información válida al {date}."

    lines = [f"Resultados al {date}:"]
    for r in filtered:
        line = f"- {r.fact if hasattr(r, 'fact') else getattr(r, 'name', 'Sin nombre')}"
        if hasattr(r, 'valid_at') and r.valid_at:
            line += f" (desde {r.valid_at.strftime('%Y-%m-%d')})"
        if hasattr(r, 'invalid_at') and r.invalid_at:
            line += f" (hasta {r.invalid_at.strftime('%Y-%m-%d')})"
        lines.append(line)
    return "\n".join(lines)

# ==================== AGENTE ====================
SYSTEM_PROMPT = """Eres un asistente inteligente que ayuda a responder preguntas usando un Knowledge Graph temporal.

## CAPACIDADES
Tienes acceso a un Knowledge Graph construido con Graphiti que contiene información sobre episodios procesados. Puedes:
- Buscar FACTS (relaciones entre entidades) usando diferentes estrategias
- Buscar ENTIDADES (personas, organizaciones, conceptos)
- Hacer queries TEMPORALES (información válida en fechas específicas)
- Explorar el GRAFO usando traversal desde entidades

## HERRAMIENTAS DISPONIBLES

1. **search_facts_semantic**: Búsqueda semántica de facts (por significado)
   - Usa cuando: la pregunta es conceptual o busca relaciones por significado
   - Ejemplo: "¿Qué proyectos tiene Juan?"

2. **search_facts_keyword**: Búsqueda por keywords exactos (BM25)
   - Usa cuando: buscas términos específicos o nombres exactos
   - Ejemplo: "PostgreSQL", "TechCorp"

3. **search_facts_hybrid**: Búsqueda híbrida (semántica + keywords + reranking)
   - Usa cuando: quieres los mejores resultados generales
   - Es la opción por defecto para búsquedas generales

4. **search_entities**: Buscar entidades (personas, organizaciones, etc.)
   - Usa cuando: quieres saber quién o qué existe en el grafo
   - Ejemplo: "¿Quién es María?"

5. **search_temporal**: Búsqueda en el tiempo (point-in-time)
   - Usa cuando: la pregunta incluye "en [fecha]", "antes de", "después de"
   - Ejemplo: "¿Dónde trabajaba Juan en marzo de 2024?"

6. **search_graph_traversal**: Exploración por traversal (BFS)
   - Usa cuando: quieres encontrar conexiones indirectas
   - Ejemplo: "¿Con quién ha trabajado Juan?"

## INSTRUCCIONES

1. **Analiza la pregunta** cuidadosamente para elegir la(s) herramienta(s) correcta(s)
2. **Usa múltiples herramientas** si es necesario para responder completamente
3. **Prioriza search_facts_hybrid** para búsquedas generales (mejor recall/precision)
4. **Usa search_temporal** cuando la pregunta mencione fechas o tiempo
5. **Sintetiza la información** de manera clara y concisa
6. **Cita las fuentes** cuando menciones facts específicos
7. **Sé honesto** si no encuentras información relevante

## FORMATO DE RESPUESTA

- Responde en español de manera natural y conversacional
- Organiza la información de forma clara (usa listas si es apropiado)
- Incluye fechas cuando sean relevantes
- Si hay información temporal, menciona la vigencia
- Si no encuentras información, di "No tengo información sobre..." y sugiere reformular

## EJEMPLOS

Pregunta: "¿En qué proyectos trabajó Juan?"
Acción: Usar search_facts_hybrid("Juan proyectos")

Pregunta: "¿Dónde trabajaba María en febrero de 2024?"
Acción: Usar search_temporal("María trabajo", "2024-02-01")

Pregunta: "¿Quiénes trabajan en TechCorp?"
Acción: Usar search_facts_keyword("TechCorp") + search_entities("TechCorp empleados")

Ahora responde las preguntas del usuario usando las herramientas apropiadas."""

agent = create_agent(
    model=llm,
    tools=[search_hybrid, search_temporal]
)

# ==================== CHATBOT (TU ORIGINAL) ====================
class Chatbot:
    def __init__(self):
        self.history: List[Any] = [SystemMessage(content=SYSTEM_PROMPT)]

    async def ask(self, q: str) -> str:
        self.history.append(HumanMessage(content=q))
        state = await agent.ainvoke({"messages": self.history})
        output = state["messages"][-1].content
        self.history.append(AIMessage(content=output))
        return output


# ==================== MAIN ====================
async def main():
    bot = Chatbot()
    print("\nChatbot listo. Escribe 'salir' para terminar.\n")

    while True:
        q = input("Tú: ").strip()
        if q.lower() in ["salir", "exit", "quit"]:
            print("¡Chau!")
            break
        if not q:
            continue
        resp = await bot.ask(q)
        print(f"Asistente: {resp}\n")


if __name__ == "__main__":
    asyncio.run(main())