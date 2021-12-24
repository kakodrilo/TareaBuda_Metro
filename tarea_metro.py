def red_expres(red, color):
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
    
    L = sorted(list(distancia.items()), key= lambda x: x[1])
    for i in L:
        if visitado[i[0]] == 0:
            return i[0]
    return -1

def dijsktra(red, inicio):
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


nombre_archivo = input('Ingrese nombre del archivo: ')

file = open(nombre_archivo)

L = file.readlines()
file.close()
N = int(L[0].strip())

L = list(map(lambda x: x.strip().split(), L))[1:]

red = {}
for i in L:
    red[i[0]] = {}
    red[i[0]]['color'] = i[-1]
    red[i[0]]['nodes'] = []
    nodes = i[2:2+int(i[1])]
    for n in nodes:
        node = list(filter(lambda x: x[0]==n,L))[0]
        red[i[0]]['nodes'].append(n)

for i in red.keys():
    st = i + ' ' + red[i]['color'] + ' -> '
    for n in red[i]['nodes']:
        st += n+' '
    print(st)

inicio = input('Ingrese estación de inicio:')
final = input('Ingrese estación de termino:')
color = input('Ingrese color del tren (rojo o verde) (opcional):')

if color == '':
    print('Mostrando todas las rutas posibles:')
    distancia, camino = dijsktra(red, inicio)
    print('Tren sin color:',camino[final])
    red_verde = red_expres(red, 'verde')
    distancia, camino = dijsktra(red_verde, inicio)
    print('Tren verde:',camino[final])
    red_roja = red_expres(red, 'rojo')
    distancia, camino = dijsktra(red_roja, inicio)
    print('Tren rojo:',camino[final])
    
elif color == 'verde' or color == 'rojo':
    print('Mostrando la ruta para tren de color',color,':')
    red_color = red_expres(red, color)
    distancia, camino = dijsktra(red_color, inicio)
    print(camino[final])
