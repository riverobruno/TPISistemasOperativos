
Simulador de la planificación de recursos y asignación de memoria de un sistema operativo, hecho en 2024 como
Trabajo Práctico Integrador de la asignatura Sistemas Operativos.

## Equipo Los Ensambladores

- Basualdo Álvarez, Facundo Fabián.
- Galarza Maumary, Florencia.
- Martínez, Agostina Denise.
- Rivero, Bruno Sebastián.
- Urturi, Renzo Octavio.
- Zeniquel Martinelli, Camila Aylén.



## Aspectos técnicos del simulador

Este proyecto es un simulador de planificación de procesos y administración de memoria en Python, que implementa un esquema de particiones fijas y utiliza Round Robin como algoritmo de planificación de CPU.

El simulador permite cargar procesos manualmente mediante una interfaz gráfica (Tkinter) o desde un archivo de texto/CSV. Gestiona la admisión, suspensión y reactivación de procesos según la disponibilidad de memoria, e imprime el estado del sistema de forma interactiva.

<ins> Funcionalidades principales </ins>
- Gestión de memoria con asignación por peor ajuste (Worst Fit) y cálculo de fragmentación interna.

- Planificación de CPU con Round Robin (quantum configurable).

- Admisión y suspensión de procesos según la multiprogramación y disponibilidad de particiones.

- Carga de procesos desde archivo o por interfaz gráfica.

- Informe estadístico al finalizar la simulación [Tiempo de retorno y de espera por proceso; promedios globales;
rendimiento del sistema (trabajos/unidad de tiempo)].

- Visualización en tablas con tabulate y colores con colorama.

<ins> Ejecución </ins>

Al iniciar, el programa solicita la forma de carga de procesos manual, con el archivo procesos.txt adjunto o cualquier .txt/.csv con formato _id_proceso,tamaño,tiempo_arribo,tiempo_irrupción_

El simulador avanza paso a paso, mostrando las colas, particiones y procesos en CPU, y espera que el usuario presione Enter para continuar.




