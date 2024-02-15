*Integrante*

Jesus Meriles
Britanny Marino

*Enunciado*

Crear una aplicacion de lista de tareas que permita a los usuarios agregar nuevas tareas, marcarlas como completadas, eliminarlas de la lista, generar reportes por estados de tareas en curso y tareas completadas.

La aplicacion debe ser implementada utilizando un lenguaje de programacion de su seleccion (por ejemplo: Python, Java oo JavaScript) y debe incluir una interfaz de comandos (CLI) para interactiar con ella (Menu de Opciones)

Se debe usar Programacion Orientada a Objetos o Programacion Modular o ambos.

*Analisis del Problema*

El problema consiste en crear una aplicacion que consiste en agregar tareas, marcar como completadas,nuevas o  en curso, se puedan eliminar de la lista, y generar reportes por estado de tareas.

La aplicacion consta en tener 3 opciones los cuales son: 1-agregar tarea, 
2-modificar tarea 
3-eliminar tarea.

La aplicacion consta de al momento de realizar la actividad en la tarea seleccionada se agregara la fecha y la hora.

Cada tarea tendra la opcion de poder colocarse el estado de trabajo los cuales seran:
1-Iniciada
2-En curso...
3-Terminado

Una vez colocado el estado de la tarea se agregara la opcion de generar reportes segun el estado de la tarea el cual sera:
1-Reporte de lista

*Diseño solucion*

Para reaizar este problema utilizaremos una estructura de clases y funciones modulares de python.Crearemos dos clases principales: Task para representar cada tarea y TaskManager para gestionar las operaciones en la lista de tareas.


Explicación del Diseño:

Clases:

-Task: Representa una tarea con una descripción y un estado predeterminado de "En curso". La función str permite imprimir de manera legible una tarea.
TaskManager: Gestiona las operaciones en la lista de tareas, como agregar, actualizar estado, eliminar y generar informes.
Funciones en TaskManager:

-add_task: Agrega una nueva tarea a la lista.
update_task_status: Actualiza el estado de una tarea existente.
delete_task: Elimina una tarea de la lista.
generate_report: Genera un informe de tareas filtrado por estado.
Interfaz de Comandos:

-display_menu: Muestra el menú de opciones al usuario.
Función Principal (main):

Un bucle que presenta el menú de opciones al usuario y ejecuta la operación correspondiente según la elección del usuario.
Este diseño utiliza programación orientada a objetos y modularidad para organizar el código de manera clara y facilitar el mantenimiento. Cada tarea es un objeto con su propio estado, y el TaskManager se encarga de administrar las operaciones sobre estas tareas. La interfaz de comandos permite una interacción fácil y amigable con la aplicación.

*PANTALLA PRINCIPAL*

https://www.canva.com/design/DAF85P190Og/X_EWIbX6zJL2MVAHeez-Nw/edit?utm_content=DAF85P190Og&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
