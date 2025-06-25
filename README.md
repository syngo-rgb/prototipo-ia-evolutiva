#**Prototipo: IA Evolutiva en entorno 2D simple**

##**Descripción**

Este proyecto es un prototipo de agente adaptativo en un entorno 2D que utiliza neuroevolución para aprender comportamientos inteligentes. Está implementado en Python, utilizando pygame para la visualización y neat-python para la evolución de redes neuronales.

El agente aprende a sobrevivir recolectando alimentos y evitando enemigos en un mundo simulado. El objetivo es demostrar cómo los algoritmos evolutivos, especialmente NEAT (NeuroEvolution of Augmenting Topologies), pueden generar agentes autónomos capaces de aprender sin programación explícita.

Este trabajo forma parte del Trabajo Práctico de la asignatura Programación de Inteligencia Artificial y Patrones de Comportamiento, correspondiente al tercer año de la Licenciatura en Producción de Videojuegos y Entretenimiento Digital de la Universidad Nacional de Rafaela (UNRAF).

###**Características principales**

    Entorno 2D simple con agente, alimentos y enemigos.

    Visualización en tiempo real con pygame.

    Evolución estructural de redes neuronales mediante neat-python.

    Evaluación basada en supervivencia y recolección de recursos.

    Código modular, fácil de entender y adaptar.

###**Requisitos**

    Python 3.7 o superior

    pygame

    neat-python

###**Instalación de dependencias:**
```
pip install pygame neat-python
```
###**Instalación y ejecución**

Clonar el repositorio:
```
git clone https://github.com/syngo-rgb/prototipo-ia-evolutiva.git
cd prototipo-ia-evolutiva
```
Ejecutar la simulación:
```
python main.py
```
Se abrirá una ventana donde se visualizará la evolución de los agentes en tiempo real.

###**Estructura del proyecto**

Archivo	Descripción
main.py	Script principal que ejecuta la simulación y NEAT.
agent.py	Implementación de la lógica y red neuronal del agente.
environment.py	Definición del entorno, alimentos y enemigos.
config-feedforward.txt	Configuración de parámetros para neat-python.
README.md	Documentación del proyecto.

###**Personalización y adaptación**

    Ajusta los parámetros evolutivos en config-feedforward.txt (mutación, población, etc.).

    Modifica la lógica en environment.py para crear nuevos desafíos.

    Extiende la capacidad del agente en agent.py añadiendo sensores o acciones.

    Integra el sistema en otros proyectos de IA, videojuegos o simulaciones.


Las contribuciones son bienvenidas.

¡Gracias por tu interés en el proyecto!
