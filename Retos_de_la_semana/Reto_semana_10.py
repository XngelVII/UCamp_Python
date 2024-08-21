######################################################################################################################
# Que permita crear dos listas de distintas longitudes
# Que la longitud de los elementos de cada lista sean especificados por el usuario
# Que imprima las listas indicando que son las listas originales
# Que elimine de la primera lista los nombres de la segunda
# Que imprima la primera lista indicando que se han eliminado los elementos que estaban tambien en la segunda
######################################################################################################################

while True:
    try:
        # Se pide al usuario ingrese la longitud de 2 listas
        long_1 = int(input('Ingresa la longitud de la primera lista: '))
        long_2 = int(input('Ingresa la longitud de la segunda lista: '))

        # Se usa input para ir agregando elementos a cada una de las listas hasta que se cubra la longitud dada en el bloque anterior
        lista_1 = [input(f'Ingresa el nombre {i+1} para la primera lista: ') for i in range(long_1)]
        lista_2 = [input(f'Ingresa el nombre {i+1} para la segunda lista: ') for i in range(long_2)]

        # Se imprimen las listas originales 
        print(f'\nListas originales:\nLista 1:{lista_1}\nLista 2:{lista_2}')

        # Se define una nueva lista sin los elementos repetidos en la lista b
        sin_duplicado = [nombre for nombre in lista_1 if nombre not in lista_2]

        # Se imprime la lista sin duplicados y cierra el programa
        print('\nLista 1 después de eliminar los elementos que están en la Lista 2:')
        print(sin_duplicado)
        print(f'\n Gracias por usar este programa')
        exit()
    # Si se ingresa un valor erroneo en la longitud de las listas envara un mensaje pidiendo usar numero.
    except ValueError:
        print(f'Por favor ingresa una longitud correcta. Usa numeros.')