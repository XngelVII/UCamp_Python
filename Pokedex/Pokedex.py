# Se importan las librerias que se van a usar
# requests para hacer peticiones a las APis
# plt para imprimir graficos
# Image para uso de imagenes
# urlopen para colectar informacion de una URL
import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

inicio_json = "{"

# Funcion pkm
def pkm():
    '''
    Funcion que le pregunta al usuario el nombre o numero del pokemon que quiere revisar
        Guarda el input del usuario y hace un request a la API
        guarda el request hecho al API en una variable, si la variable es diferente de 200 entonces le informa al usuario que el pokemon no ha sido encontrado
        el el mensaje del request hecho a la API es 200 entonces guarda el .json en una variable
        se definen las variables de los datos de los pokemones tomadas del json 
        luego de definidas las variables de los datos de los pokemones se llama a la funcion check_image para confirmar que exista una imagen.
    '''
    # Saludo al usuario y se le pide ingrese el nombre del monstruo que quiere revisar
    pkm = input('-----------------------------------------------\nPor favor ingresa el NOMBRE o NUMERO del Pokemon que quieres revisar: ').lower()
    # Se define una variable como la direccion del API + el nombre del pokemon
    url = 'https://pokeapi.co/api/v2/pokemon/' + pkm
    respuesta = requests.get(url) # Se usa el .get para obtener informacion de la URL 
    # Si la peticion devuelve un codigo diferente de 200 envia un mensaje de pokemon no encontrado y sale del programa
    if respuesta.status_code != 200:
        print('-----------------------------------------------\nPokemon no encontrado\n-----------------------------------------------\n')
    # Se define una variable que contendra toda la informacion del .json obtenido de la API
    else:
        datos = respuesta.json() 
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
        # Se definen variables que contienen los atributos del pokemon a revisar tomando la informacion de la variable datos (que tiene la informacion del pokemon en json)
        url_imagen = datos['sprites']['front_default']
        # Se llama la funcion siguente
        check_imagen(datos, url_imagen, nombre, peso, altura, movimientos, habilidades, tipos)

# Funcion que hace solicitudes a la API 
def check_imagen(datos, url_imagen, nombre, peso, altura, movimientos, habilidades, tipos):
    '''
    Funcion que hace la solicitud de datos a la API
        Revisa que la exista la imagen del pokemon buscado
        si existe va abrir la imagen y va manda llamar la funcion mostrar_pkm
        si no existe entonces le informa al usuario y llama a la funcion pkm()
    '''
    try:
        # Condicional que aplica si existe la variable url_imagen entonces va a abrir la imagen de la url y va a llamar a la funcion mostrar_pkm
        if url_imagen:  
            imagen = Image.open(urlopen(url_imagen))
            mostrar_pkm(imagen, datos, nombre, peso, altura, movimientos, habilidades, tipos, url_imagen)
        # Si la variable url_imagen esta vacia, se mostrara un mensaje indicandoselo al usuario y volvera al incio
        else:
            print('-----------------------------------------------\nEl Pokemon no tiene imagen disponible.\n-----------------------------------------------\n')
            pmk()
    except:
        print('-----------------------------------------------\nNo se pudo obtener la imagen del Pokemon.\n-----------------------------------------------\n')
        exit()

# Funcion para mostrar el pokemon y los datos del mismo
def mostrar_pkm(imagen, datos, nombre, peso, altura, movimientos, habilidades, tipos, url_imagen):
    '''
    Funcion para mostrar los datos del pokemon buscado
        Imprime en la terminal nombre, peso, altura tipos, habilidades y movimientos del pokemon buscado
        guarda la imagen obtenida de la API de pokemon 
        muestra la imagen en un grafico sin ejes
    '''
    # Se muestra en la terminal la informacion del pokemon buscado
    print(f'-----------------------------------------------')
    print(f'Nombre:\t\t{nombre}')
    print(f'Peso:\t\t{peso:.1f} KG')
    print(f'Altura:\t\t{altura:.1f} M')
    print(f'Tipos:\t\t{tipos}')
    print(f'Habilidades:\t{habilidades}')
    print(f'Movimientos:\t{movimientos}')
    print(f'-----------------------------------------------')
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
    '''
    Funcion que guarda la informacion del pokemon en un archivo .json
        Crea un archivo archivo .json y lo nombra como el pokemon que busque el usuario
        escribe en el archivo nombre, peso, altura, tipos, habilidades movimientos y la url de la imagen del pokemon
        agrega {} al inicio y al final para darme el "formato" json
        cierra el archivo
    '''
    # Se usa un open/as para ir agregando la informacion al archivo.json. El archivo .json tendra el nombre del pokemon buscado 
    with open(f'{nombre}.json','w') as f_archivo:
        # Estos son los datos que se van a agregar al archivo .json del pokemon
        f_archivo.write(f'{inicio_json}\n"Nombre": {nombre}\n')
        f_archivo.write(f'"Peso": {peso:.1f} KG\n')
        f_archivo.write(f'"Altura": {altura:.1f} M\n')
        f_archivo.write(f'"Tipos": {tipos}\n')
        f_archivo.write(f'"Habilidades": {habilidades}\n')
        f_archivo.write(f'"Movimientos": {movimientos}\n')
        f_archivo.write(f'"Imagen": {url_imagen} \n'"}"  )
        f_archivo.close()

# Funcion pirncipal
def main():
    '''
    Funcion principal 
        Saluda al usuario
        Le da 2 opciones
        1 buscar un pokemon. llama a la funcion pkm()
        2 salir envia un mensaje de despedida y sale del programa
    '''
    # Msensaje de bienvenida para el usuario
    print('-----------------------------------------------\nHola soy una Pokedex n_n!')
    # Ciclo while para que el usuario escoga una de las dos opciones (buscar) o (salir)
    while True:
        try:
            opcion = input(f'-----------------------------------------------\nQue quieres hacer?:\n\t(1) Buscar un Pokemon.\n\t(2) Salir.\n-----------------------------------------------\n\t')
            if opcion == '1':
                pkm()
            elif opcion == '2':
                print(f'-----------------------------------------------\n\tGracias por usar esta Pokedex.\n\t\tHasta pronto.\n-----------------------------------------------\n')
                exit()
            else:
                print(f'-----------------------------------------------\nPor favor selecciona una opcion valida.\n-----------------------------------------------')
        except ValueError:
            print('-----------------------------------------------\nDisculpa, pero algo salio muy mal UwU.\n-----------------------------------------------\n')

main()
