from funciones import dijsktra, red_expres
#####################################################

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
