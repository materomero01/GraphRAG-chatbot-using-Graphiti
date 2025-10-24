# 🤖 Graphiti Gemini Chatbot: Knowledge Graph Temporal

Este proyecto demuestra cómo construir un Knowledge Graph (Grafo de Conocimiento) temporal utilizando la librería **Graphiti** y la IA de **Google Gemini** para luego interactuar con él mediante un agente de LangChain. El grafo se enfoca en mantener un registro de hechos con su periodo de validez.

## 🚀 Requisitos

Para ejecutar el proyecto necesitas tener instalado:

1.  **Python 3.9+**
2.  **Neo4j Desktop o Server** ejecutándose localmente.
3.  Una **clave API de Gemini** (disponible en Google AI Studio).

## 1. Instalación de Dependencias

Se recomienda encarecidamente usar un entorno virtual para aislar las dependencias:

# Crear entorno virtual (si no existe)
python -m venv venv

# Activar el entorno virtual
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instalar los paquetes necesarios
pip install -r requirements.txt

## 2. Configuración del Entorno (.env)
Crea un archivo llamado .env en la raíz del proyecto y configúralo con tus credenciales.

Fragmento de código

# Reemplaza con tu clave de API de Gemini
GEMINI_API_KEY="TU_CLAVE_API_DE_GEMINI_AQUI"

# Configuración de la base de datos Neo4j
NEO4J_URI="bolt://localhost:7687"
NEO4J_USER="neo4j"
NEO4J_PASSWORD="TU_CONTRASEÑA_DE_NEO4J"


## 3. Uso del Proyecto
El flujo de trabajo consta de tres scripts: limpiar (opcional), construir el grafo e interactuar con el chatbot.

# 3.1. Limpiar el Grafo (Opcional)
Si necesitas borrar todas las entidades y relaciones del grafo (para una ejecución limpia):
ejecuta: python clear_knowledge_graph.py
Este script elimina todos los nodos y relaciones de la instancia de Neo4j configurada en el archivo .env.

# 3.2. Construir el Knowledge Graph
Para cargar los datos de ejemplo (los episodios definidos en el archivo) en el Knowledge Graph, ejecuta:

ejecuta: python build_knowledge_graph.py

⚠️ Advertencia: Este script incluye un delay_between_episodes de 10.0 segundos para evitar límites de tasa de la API de Gemini. La ejecución es intencionadamente lenta para asegurar que todos los episodios sean procesados correctamente.

Al finalizar, el grafo estará cargado con el dataset temporal y listo para ser consultado.

# 3.3. Iniciar el Chatbot e Interactuar
Una vez que el grafo está cargado, puedes iniciar el asistente inteligente. El script chatbot.py inicializa un agente de LangChain que utiliza el modelo Gemini para interpretar tu pregunta y las herramientas de Graphiti para buscar respuestas en el grafo.

ejecuta: python chatbot.py
El chatbot te pedirá que escribas una pregunta.

## 💬 Ejemplos de Preguntas (Basadas en el dataset cargado):
¿Qué cargo tenía Juan el 2024-03-01? (Usa búsqueda temporal)

¿Quién se unió al equipo de Juan en febrero de 2024?

¿Cuándo fue promovido Juan?

¿Dónde tiene oficinas TechCorp?

¿Qué proyectos lideró Juan?
