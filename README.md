# Tarea Buda - Metro

Tarea de proceso de postulación a puesto de desarrollador full stack en buda.com

## Comentario general
Se presenta la resolución de la tarea indicada en el archivo _Tarea_Buda.com_-_Metro.pdf_. Fue necesaria una propuesta de archivo de entrada que permita codificar una red de metros con sus distintas propiedades como lo son conexiones y colores. Se buscó plantear una propuesta de archivo simple, que permita fáciles modificaciones, y se dejó el calculo de rutas _express_ para tiempo de ejecución cuando fueran necesarias. 

Ya que la red de metros se puede interpretar como un grafo, donde las estaciones son los nodos y las aristas indican si se puede llegar de una estación a otra, se decidió utilizar el algoritmo _Dijsktra_, y así calcular la distancia y el camino mínimo entre el nodo inicial y todos los nodos de la red. 

El algoritmo propuesto fue desarrollado en _Python_ en su  versión 3.9.4, y no se utilizó ninguna librería.

Por último, para evaluar el correcto funcionamiento de las funciones construidas para la solución propuesta, se desarrollaron pruebas automáticas a través de la librería _Pytest_.
## Formato de archivo de entrada

Al tratarse sobre una red de metros se consideró la construcción de un grafo a través de una lista de adyacencia. El archivo debe contener la cantidad de estaciones, seguido por el nombre de estación, a qué otras estaciones está conectada y el color de la estación (rojo, verde o null.
Por ejemplo, para construir la red:
![](https://cdn.discordapp.com/attachments/425837581557694474/924036023623761960/unknown.png)
se considera el siguiente archivo:
<pre><code>9
A 1 B null
B 2 A C null
C 3 B D G null
D 2 C E null
E 2 D F null
F 2 E I null
G 2 C H verde
H 2 G I rojo
I 2 H F verde
</code></pre>

Destacar que el calculo de rutas express se hace en tiempo de ejecución y sólo si es necesario. En el ejemplo, la red propuesta está en el archivo _red.txt_.

## Ejecución
Para la ejecución del algoritmo se utiliza el siguiente comando:

<pre><code>python main.py
</code></pre>
en la ejecución se solicitarán 4 parámetros:
* nombre del archivo donde esta la red de metro a considerar
* nombre de la estación inicial
* nombre de la estación objetivo
* color del tren (rojo o verde) (opcional)

### Ejemplo de ejecución
<pre><code>Ingrese nombre del archivo: red.txt
Ingrese estación de inicio:A
Ingrese estación de termino:F
Ingrese color del tren (rojo o verde) (opcional):
Mostrando todas las rutas posibles:
Tren sin color: A->B->C->D->E->F
Tren verde: A->B->C->D->E->F
Tren rojo: A->B->C->H->F
</code></pre>


## Test automáticos
Se consideraron 9 pruebas automáticas, que evalúan a 2 de las funciones creadas. Se consideran casos bordes, y casos a partir del ejemplo propuesto. 
Para la ejecución de las pruebas se debe utilizar el comando:

<pre><code>pytest</code></pre>

esto evaluará las 9 pruebas presentes en el archivo *test_funciones.py*.