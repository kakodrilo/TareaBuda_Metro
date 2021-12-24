def red_expres(red, color):
    """
    Funcion que toma una red de metro completa y un color de tren. 
    Devuelve una nueva red solo con las rutas que puede recorrer el tren de color senialado
    ///
    Args:
        red (dict): red de metro completa
        color (string): color del tren
    return:
        diccionario con la lista de adyacencia de cada estacion
    """
    visitado = {}
    red_color = {}
    for i in red.keys():
         visitado[i] = 0

    for i in red.keys():
        red_color[i] = {'nodes':[]}
        if red[i]['color'] in [color,'null']:
            for n in red[i]['nodes']:
                if red[n]['color'] in [color,'null']:
                    red_color[i]['nodes'].append(n)
                else:
                    vecinos = red[n]['nodes'].copy()
                    while len(vecinos) > 0:
                        v = vecinos.pop(0)
                        if i != v and red[v]['color'] in [color,'null']:
                            red_color[i]['nodes'].append(v)
                            vecinos = []
                        else: 
                            vecinos = vecinos + red[v]['nodes'].copy()
    return red_color

def minimo_no_visitado(visitado, distancia):
    """
    Funcion auxiliar de dijsktra que entrega la estacion aun no visitada con menor distancia al inicio.
    ///
    Args:
        visitado (dict): diccionario que indica si las estaciones estan visitadas o no
        distancia (dict): diccionario que indica la distancia actual de las estaciones al inicio
    return:
        nombre de la estacion aun no visitada y mas cercana al inicio o -1 en caso de que ya todas esten visitadas.
    """
    L = sorted(list(distancia.items()), key= lambda x: x[1])
    for i in L:
        if visitado[i[0]] == 0:
            return i[0]
    return -1

def dijsktra(red, inicio):
    """
    Funcion que calcula la distancia y el camino minimo desde un nodo de inicio hacia todos los demas
    ///
    Args:
        red (dict): diccionario con la red en forma de lista de adyacencia
        inicio (string): nombre de la estacion de inicio
    return:
        dos diccionarios, uno indicando el largo del camino, y el otro indicando el camino.
    """
    N = len(list(red.keys()))
    distancia = {}
    visitado = {}
    camino = {}
    for i in red.keys():
        distancia[i] = float('inf')
        visitado[i] = 0
        camino[i]=''
    distancia[inicio] = 0
    camino[inicio] = inicio
    
    for i in range(N):
        curr = minimo_no_visitado(visitado, distancia)
        visitado[curr] = 1
        
        for j in red[curr]['nodes']:
            if visitado[j[0]] == 0 and distancia[curr] + 1 < distancia[j[0]]:
                distancia[j[0]] = distancia[curr] + 1
                camino[j[0]] = camino[curr] + '->'+j[0]
    
    return distancia,camino
