# 🤖 Graphiti Gemini Chatbot: Knowledge Graph Temporal

Este proyecto demuestra cómo construir un Knowledge Graph (Grafo de Conocimiento) temporal utilizando la librería **Graphiti** y la IA de **Google Gemini** para luego interactuar con él mediante un agente de LangChain. El grafo se enfoca en mantener un registro de hechos con su periodo de validez.

## 🚀 Requisitos

Para ejecutar el proyecto necesitas tener instalado:

1.  **Python 3.9+**
2.  **Neo4j Desktop o Server** ejecutándose localmente.
3.  Una **clave API de Gemini** (disponible en Google AI Studio).

## 1. Instalación de Dependencias

Se recomienda encarecidamente usar un entorno virtual para aislar las dependencias:

```bash
# Crear entorno virtual (si no existe)
python -m venv venv

# Activar el entorno virtual
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instalar los paquetes necesarios
pip install -r requirements.txt
