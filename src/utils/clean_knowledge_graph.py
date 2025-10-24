import asyncio
import os
from dotenv import load_dotenv
from graphiti_core import Graphiti
from graphiti_core.llm_client.gemini_client import GeminiClient, LLMConfig
from graphiti_core.embedder.gemini import GeminiEmbedder, GeminiEmbedderConfig
from graphiti_core.cross_encoder.gemini_reranker_client import GeminiRerankerClient

# Cargar variables de entorno
load_dotenv()

# ==================== CONFIGURACIÓN ====================

# Se requieren solo las credenciales de Neo4j para la limpieza
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Aunque no se usan para la limpieza, Graphiti requiere clientes LLM válidos
# Si GEMINI_API_KEY no está disponible, se puede usar una clave dummy
def get_dummy_api_key():
    return GEMINI_API_KEY if GEMINI_API_KEY else "dummy_key_for_graphiti_init"

async def initialize_graphiti_for_admin() -> Graphiti:
    """Inicializa Graphiti con clientes dummy o reales solo para acceder al driver de Neo4j."""
    print("Inicializando Graphiti para operación de limpieza...")
    
    api_key = get_dummy_api_key()

    llm_client = GeminiClient(config=LLMConfig(api_key=api_key, model="gemini-2.5-flash"))
    embedder = GeminiEmbedder(config=GeminiEmbedderConfig(api_key=api_key, embedding_model="text-embedding-004"))
    reranker = GeminiRerankerClient(config=LLMConfig(api_key=api_key, model="gemini-2.5-flash"))

    graphiti = Graphiti(
        NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD,
        llm_client=llm_client,
        embedder=embedder,
        cross_encoder=reranker,
    )
    
    print("Graphiti inicializado.")
    return graphiti

async def clear_graph(graphiti: Graphiti):
    """Ejecuta consultas Cypher para eliminar todos los datos."""
    print("\n" + "=" * 50)
    print("🧹 INICIANDO LIMPIEZA TOTAL DEL GRAFO 🧹")
    print("=" * 50)

    try:
        # 1. Borrar nodos y relaciones
        print("1. Borrando todas las relaciones y nodos...")
        async with graphiti.driver.session() as session:
            # Eliminar todos los nodos y relaciones
            await session.run("MATCH (n) DETACH DELETE n")

        print("✅ Nodos y relaciones eliminados.")

        # 2. Reemplazar la sección que falló con una notificación:
        print("2. Saltando restablecimiento de esquema (métodos obsoletos/inexistentes en la versión de Graphiti).")
        print("El script build_knowledge_graph.py se encargará de crear los índices si son necesarios.")


        print("\n" + "=" * 50)
        print("✨ LIMPIEZA COMPLETA: El Knowledge Graph está vacío. ✨")
        print("=" * 50)

    except Exception as e:
        print(f"\n❌ ERROR FATAL DURANTE LA LIMPIEZA: {str(e)}")
        print("Asegúrate de que la base de datos Neo4j esté corriendo.")

        
async def main():
    try:
        graphiti = await initialize_graphiti_for_admin()
        await clear_graph(graphiti)
    except Exception as e:
        print(f"Error en la ejecución principal: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())