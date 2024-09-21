# Se importan las librerias que se van a usar
# requests para hacer peticiones a las APis
# plt para imprimir graficos
# Image para uso de imagenes
# urlopen para colectar informacion de una URL
import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

# Funcion principal
def main():
    # Saludo al usuario y se le pide ingrese el nombre del monstruo que quiere revisar
    pkm = input('Hola, soy una pokedex.\nPor favor ingresa el nombre o numero del pokemon que quieres revisar: ').lower()
    # Se define una variable como la direccion del API + el nombre del pokemon
    url = 'https://pokeapi.co/api/v2/pokemon/' + pkm
    respuesta = requests.get(url) # Se usa el .get para obtener informacion de la URL 
    # Si la peticion devuelve un codigo diferente de 200 envia un mensaje de pokemon no encontrado y sale del programa
    if respuesta.status_code != 200:
        print('Pokemon no encontrado')
        exit()

    # Se define una variable que contendra toda la informacion del .json obtenido de la API
    datos = respuesta.json() 
    # Se definen variables que contienen los atributos del pokemon a revisar tomando la informacion de la variable datos (que tiene la informacion del pokemon en json)
    url_imagen = datos['sprites']['front_default']
    nombre = datos['name']
    nombre = nombre.capitalize()
    # Busque en la wiki de pokemon en que unidades estaba el peso y la altura el peso y la altura
    # Tuve que multiplicar por 0.1 para convertir el peso a KG y la altura a M
    peso = datos['weight']*0.1
    # peso = peso*0.1 
    altura = datos['height']*0.1
    movimientos = [movimiento['move']['name'] for movimiento in datos['moves']]
    habilidades = [habilidad['ability']['name'] for habilidad in datos['abilities']]
    tipos = [tipo['type']['name'] for tipo in datos['types']]
    # Se llama la funcion siguente
    llamada_de_API(datos, url_imagen, nombre, peso, altura, movimientos, habilidades, tipos)

# Funcion que hace solicitudes a la API 
def llamada_de_API(datos, url_imagen, nombre, peso, altura, movimientos, habilidades, tipos):
    try:
        # Condicional que aplica si existe la variable url_imagen entonces va a abrir la imagen en la url y va a llamar a la funcion mostrar_pkm
        if url_imagen:  
            imagen = Image.open(urlopen(url_imagen))
            mostrar_pkm(imagen, datos, nombre, peso, altura, movimientos, habilidades, tipos, url_imagen)
        # Si la variable url_imagen esta vacia, se mostrara un mensaje indicandoselo al usuario y volvera al incio
        else:
            print('El pokemon no tiene imagen disponible.')
            main()
    except:
        print('No se pudo obtener la imagen del Pokemon.')
        exit()

# Funcion para mostrar el pokemon y los datos del mismo
def mostrar_pkm(imagen, datos, nombre, peso, altura, movimientos, habilidades, tipos, url_imagen):
    # Se muestra en la terminal la informacion del pokemon buscado
    print(f'Nombre:\t\t{nombre}')
    print(f'Peso:\t\t{peso:.1f} KG')
    print(f'Altura:\t\t{altura:.1f} M')
    print(f'Tipos:\t\t{tipos}')
    print(f'Habilidades:\t{habilidades}')
    print(f'Movimientos:\t{movimientos}')
    # Se manda a llamar a la funcion guardar_info
    guardar_info(datos, url_imagen, nombre, peso, altura, movimientos, habilidades, tipos)
    # Se crea un grafico que llevara como titulo el nombre del pokemon
    plt.title(nombre)
    # Enviara la imagen en el grafico
    plt.imshow(imagen)
    # Eliminara los ejes del grafico
    plt.axis('off') 
    # Mostrara el grafico
    plt.show()

# Funcion para guardar la informacion del pokemon en un archivo .json
def guardar_info(datos, url_imagen, nombre, peso, altura, movimientos, habilidades, tipos):
    # Se usa un open/as para ir agregando la informacion al archivo.json. El archivo .json tendra el nombre del pokemon buscado 
    with open(f'{nombre}.json','w') as f_archivo:
        # Estos son los datos que se van a agregar al archivo .json del pokemon
        f_archivo.write(f'Nombre: {nombre} | ')
        f_archivo.write(f'Peso: {peso:.1f} KG | ')
        f_archivo.write(f'Altura: {altura:.1f} M | ')
        f_archivo.write(f'Tipos: {tipos} | ')
        f_archivo.write(f'Habilidades: {habilidades} | ')
        f_archivo.write(f'Movimientos: {movimientos} | ')
        f_archivo.write(f'Imagen: {url_imagen} | ')

main()
