# Definicion de un diccionario con todas las letras
alfa = {
"a" : 0,
"b" : 1,
"c" : 2,
"d" : 3,
"e" : 4,
"f" : 5,
"g" : 6,
"h" : 7,
"i" : 8,
"j" : 9,
"k" : 10,
"l" : 11,
"m" : 12,
"n" : 13,
"ñ" : 14,
"o" : 15,
"p" : 16,
"q" : 17,
"r" : 18,
"s" : 19,
"t" : 20,
"u" : 21,
"v" : 22,
"w" : 23,
"x" : 24,
"y" : 25,
"z" : 26
}

# Mensaje de saludo al usuario e instrucciones
print('Hola, este programa te dira cuales son la letra anterior y siguiente a la letra que le ingreses.\n Para salir escribe la palabra exit\n\n')
while True:
    try:
        # Se pide al usuario que ingrese una letra y se guarda en la variable del mismo nombre
        letra = input('Por favor ingresa una letra:\n').lower()
        if letra == "exit":
                print('Gracias por usar este programa n_n')
                break
        # Este if garantiza que el usuario solo ingrese una letra y que dicha letra este en el diccionario definido
        if len(letra) == 1 and letra in alfa:
            print(f'La letra que ingresaste fue: {letra}')
            # Se definen 2 variables como el elemento en el diccionario mas/menos 1
            letra_mas = alfa[letra] + 1
            letra_menos = alfa[letra] - 1
            # Se definen 3 casos en los siguientes condicionales
            # Si el elemento del diccionario es 0 no hay letra anterior
            # Si el elemento del diccionario es 26 no hay letras posterior
            # Si el elemento del diccionario no es 26 o 0 se muestran las respectivas letras 
            if 26 > alfa[letra] > 0:    
                # Encontre el siguiente codigo para introduciendo un elemento del diccionario se imprima la llave
                # https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
                print(f'La letra siguiente es: {list(alfa.keys())[list(alfa.values()).index(letra_mas)]}')
                print(f'La letra anterior es: {list(alfa.keys())[list(alfa.values()).index(letra_menos)]}\n')
            elif alfa[letra] == 26:
                print(f'La letra anterior es: {list(alfa.keys())[list(alfa.values()).index(letra_menos)]}')
                print(f'No hay una letra despues de la {letra}\n')
            elif alfa[letra] == 0:
                print(f'La letra siguiente es: {list(alfa.keys())[list(alfa.values()).index(letra_mas)]}')    
                print(f'No hay una letra antes de la {letra}\n')
        # Si el usuario ingresa mas de una letra o algo que no sea una letra arrojara el siguiente mensaje
        else:
            print(f'Por favor ingresa solo una letra, no uses numeros.\n Para salir ingresa la palabra exit.')
    # Si el usuario ingresa una llave que no esta en el diccionario arrojara el siguiente error
    except KeyError:
        print('Algo salio mal uwu')
