"""
Graphiti Knowledge Graph Builder con Gemini
============================================
Script para construir un Knowledge Graph usando Graphiti con Gemini API (gratis).
Optimizado para evitar rate limits de la API gratuita de Gemini.
"""

import asyncio
import os
from datetime import datetime, timezone
from typing import List, Dict
from dotenv import load_dotenv
from graphiti_core import Graphiti
from graphiti_core.llm_client.gemini_client import GeminiClient, LLMConfig
from graphiti_core.embedder.gemini import GeminiEmbedder, GeminiEmbedderConfig
from graphiti_core.cross_encoder.gemini_reranker_client import GeminiRerankerClient

# Cargar variables de entorno desde .env
load_dotenv()

# ==================== CONFIGURACIÓN ====================

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ==================== DATOS DE EJEMPLO ====================

EPISODES = [
    {
        "content": "Juan Pérez comenzó a trabajar como Desarrollador Senior en TechCorp el 15 de enero de 2024. Su especialidad es Python y tiene 5 años de experiencia en desarrollo backend.",
        "timestamp": "2024-01-15T09:00:00Z",
        "name": "Contratación de Juan"
    },
    {
        "content": "TechCorp es una empresa de tecnología fundada en 2018 en Buenos Aires, Argentina. Se especializa en desarrollo de software para startups y tiene 50 empleados.",
        "timestamp": "2024-01-15T10:00:00Z",
        "name": "Información de TechCorp"
    },
    {
        "content": "Juan lideró el proyecto de migración de la base de datos de PostgreSQL a MongoDB. El proyecto comenzó el 1 de febrero de 2024 y requirió 3 meses de trabajo.",
        "timestamp": "2024-02-01T09:00:00Z",
        "name": "Inicio Proyecto Migración"
    },
    {
        "content": "María García se unió al equipo de Juan como Desarrolladora Junior el 15 de febrero de 2024. Ella tiene experiencia en React y Node.js.",
        "timestamp": "2024-02-15T09:00:00Z",
        "name": "María se une al equipo"
    },
    {
        "content": "El proyecto de migración se completó exitosamente el 30 de abril de 2024. Juan y María trabajaron juntos en la implementación final.",
        "timestamp": "2024-04-30T18:00:00Z",
        "name": "Finalización del proyecto"
    },
    {
        "content": "Juan fue promovido a Tech Lead el 1 de mayo de 2024 debido a su excelente desempeño en el proyecto de migración. Su nuevo salario es de $5000 USD mensuales.",
        "timestamp": "2024-05-01T09:00:00Z",
        "name": "Promoción de Juan"
    },
    {
        "content": "TechCorp abrió una nueva oficina en Córdoba, Argentina el 15 de junio de 2024. La nueva oficina tiene capacidad para 20 empleados.",
        "timestamp": "2024-06-15T10:00:00Z",
        "name": "Nueva oficina Córdoba"
    },
    {
        "content": "María comenzó a trabajar en el proyecto de desarrollo de una API REST para clientes móviles el 1 de julio de 2024. Usa FastAPI y PostgreSQL.",
        "timestamp": "2024-07-01T09:00:00Z",
        "name": "María inicia nuevo proyecto"
    },
    {
        "content": "Juan y María asistieron a la conferencia PyConAr en Buenos Aires del 10 al 12 de agosto de 2024. Conocieron a varios desarrolladores de la comunidad Python.",
        "timestamp": "2024-08-10T09:00:00Z",
        "name": "Asistencia a PyConAr"
    },
    {
        "content": "TechCorp contrató a 10 nuevos desarrolladores en septiembre de 2024. El equipo de Juan ahora tiene 5 personas: Juan como líder, María, y tres nuevos developers junior.",
        "timestamp": "2024-09-01T09:00:00Z",
        "name": "Expansión del equipo"
    },
    {
        "content": "Juan está considerando cambiar a una nueva empresa. Ha recibido una oferta de GlobalTech por $7000 USD mensuales. Está evaluando la propuesta durante octubre de 2024.",
        "timestamp": "2024-10-15T09:00:00Z",
        "name": "Juan evalúa nueva oferta"
    }
]


async def initialize_graphiti() -> Graphiti:
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY no configurada.")

    print("Inicializando Graphiti con Gemini...")
    
    llm_client = GeminiClient(config=LLMConfig(api_key=GEMINI_API_KEY, model="gemini-2.5-flash"))
    embedder = GeminiEmbedder(config=GeminiEmbedderConfig(api_key=GEMINI_API_KEY, embedding_model="text-embedding-004"))
    reranker = GeminiRerankerClient(config=LLMConfig(api_key=GEMINI_API_KEY, model="gemini-2.5-flash"))

    graphiti = Graphiti(
        NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD,
        llm_client=llm_client,
        embedder=embedder,
        cross_encoder=reranker,
    )
    
    print("Graphiti inicializado correctamente")
    return graphiti

async def add_episodes_with_rate_limit(
    graphiti: Graphiti,
    episodes: List[Dict],
    delay_between_episodes: float = 60.0,  # 60s para free tier (15 RPM)
    max_attempts: int = 3
):
    """
    Agrega episodios al grafo con delays, reintentos y manejo de rate limits.
    """
    print(f"\nProcesando {len(episodes)} episodios...")
    print(f"Delay entre episodios: {delay_between_episodes}s")
    print(f"Máximo de intentos por episodio: {max_attempts}")
    print("=" * 60)
    
    failed_episodes = []
    previous_uuids = []  # Para temporalidad

    # Ordenar por timestamp
    sorted_episodes = sorted(
        episodes,
        key=lambda x: datetime.fromisoformat(x['timestamp'].replace('Z', '+00:00'))
    )

    for i, episode in enumerate(sorted_episodes, 1):
        for attempt in range(1, max_attempts + 1):
            try:
                print(f"\n[{i}/{len(sorted_episodes)}] Procesando: {episode['name']} (Intento {attempt})")
                print(f"   Timestamp: {episode['timestamp']}")
                print(f"   Preview: {episode['content'][:80]}...")

                # Normalizar timestamp
                try:
                    episode_time = datetime.fromisoformat(
                        episode['timestamp'].replace('Z', '+00:00')
                    )
                    if episode_time.tzinfo is None:
                        episode_time = episode_time.replace(tzinfo=timezone.utc)
                except Exception as e:
                    print(f"   Error en timestamp: {e}. Usando UTC now.")
                    episode_time = datetime.now(timezone.utc)

                # Agregar episodio
                result = await graphiti.add_episode(
                    name=episode['name'],
                    episode_body=episode['content'],
                    source_description=f"Episodio {i}",
                    reference_time=episode_time,
                    previous_episode_uuids=previous_uuids  # Temporalidad
                )

                # Guardar UUID para el siguiente
                previous_uuids.append(result.episode.uuid)

                print(f"   Episodio agregado (UUID: {result.episode.uuid[:8]})")
                break

            except RateLimitError as e:
                wait = 60  # Gemini dice ~46s, redondeamos
                print(f"   Rate limit. Esperando {wait}s...")
                await asyncio.sleep(wait)
                if attempt == max_attempts:
                    failed_episodes.append((i, episode['name'], "Rate limit"))
                continue

            except Exception as e:
                print(f"   Error: {str(e)}")
                if attempt < max_attempts:
                    wait = delay_between_episodes * (2 ** (attempt - 1))  # Backoff
                    print(f"   Reintentando en {wait}s...")
                    await asyncio.sleep(wait)
                else:
                    print(f"   Fallo tras {max_attempts} intentos.")
                    failed_episodes.append((i, episode['name'], str(e)))

        # Delay entre episodios (solo si no falló)
        if i < len(sorted_episodes):
            print(f"   Esperando {delay_between_episodes}s antes del siguiente...")
            await asyncio.sleep(delay_between_episodes)

    print("\n" + "=" * 60)
    if failed_episodes:
        print(f"{len(failed_episodes)} episodios fallaron:")
        for idx, name, error in failed_episodes:
            print(f"   • {name}: {error}")
    else:
        print("Todos los episodios procesados correctamente")

    return failed_episodes

async def show_graph_stats(graphiti: Graphiti):
    print("\n" + "=" * 60)
    print("ESTADÍSTICAS DEL GRAFO")
    print("=" * 60)
    
    try:
        # Búsqueda de prueba
        results = await graphiti.search(query="Juan Pérez", num_results=5)
        print(f"\nBúsqueda: 'Juan Pérez' → {len(results)} resultados")
        for i, r in enumerate(results[:3], 1):
            fact = r.fact if hasattr(r, 'fact') else getattr(r, 'name', 'Unknown')
            print(f"   {i}. {fact}")
        
        # Relaciones temporales
        temp_results = await graphiti.search(query="Tech Lead", num_results=5)
        if temp_results:
            print(f"\nRelaciones temporales detectadas:")
            for r in temp_results:
                if hasattr(r, 'fact'):
                    v = r.valid_at.strftime('%Y-%m-%d') if hasattr(r, 'valid_at') and r.valid_at else 'None'
                    i = r.invalid_at.strftime('%Y-%m-%d') if hasattr(r, 'invalid_at') and r.invalid_at else 'None'
                    print(f"   • {r.fact} (desde: {v}, hasta: {i})")

    except Exception as e:
        print(f"No se pudieron obtener estadísticas: {str(e)}")


async def main():
    print("\n" + "=" * 60)
    print("GRAPHITI KNOWLEDGE GRAPH BUILDER")
    print("=" * 60)

    try:
        # 1. Inicializar
        graphiti = await initialize_graphiti()

        # 2. Agregar episodios (ordenados)
        failed = await add_episodes_with_rate_limit(
            graphiti,
            EPISODES,
            delay_between_episodes=10.0,  # Aumentado para evitar 503
            max_attempts=3
        )

        # 3. Estadísticas
        await show_graph_stats(graphiti)

        if failed:
            print(f"\nProceso completado con {len(failed)} errores.")
        else:
            print("\nProceso completado exitosamente!")

        print("\nPróximos pasos:")
        print("   1. Abre Neo4j Browser → http://localhost:7474")
        print("   2. Ejecuta: MATCH ()-[r]->() WHERE r.valid_at IS NOT NULL RETURN r LIMIT 10")
        print("   3. Prueba el chatbot con: ¿Qué cargo tenía Juan el 2024-03-01?")

    except Exception as e:
        print(f"\nError fatal: {str(e)}")
        raise
    finally:
        print("\n" + "=" * 60)


if __name__ == "__main__":
    asyncio.run(main())