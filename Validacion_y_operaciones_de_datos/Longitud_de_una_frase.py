# Mensaje de saludo para el Usuario asi como instruccion para salir del programa.
print(f"\nHola, este es un programa que te dice cuantas letras tiene la palabra que escribas.\n\nSi quieres salir escribe la palabra exit.\n")
# While para que se el programa se ejecute recursivamente.
while True:
    try:
        # Mensaje para que el usuario ingrese una palabra.
        palabra = input(str("Por favor introduce una palabra:"))
        # if para identificar las palabras con la longitud correcta (4 - 8 letras) diferente de la palabra para salir 'exit'.
        if 3 < len(palabra) < 9 and palabra != "exit":
            print(f"\nLa palabra es {palabra} y tiene {len(palabra)} letras. Su longitud es correcta.\n")
        # elif para palabras menores a 4 letras con sus propias condicionales para si falta 1 letra o mas letras.
        elif len(palabra) < 4:
            faltan = 4 - len(palabra) 
            if faltan == 1:
                print(f"\nLa palabra {palabra.upper()} solo tiene {len(palabra)} letras. \nFalta {faltan} letra.\n")                
            else:
                print(f"\nLa palabra {palabra.upper()} solo tiene {len(palabra)} letras. \nFaltan {faltan} letras.\n")             
        # elif para palabras mayores a 8 letras con sus propias condicionales para si sobre 1 letra o mas letras.
        elif len(palabra) > 8:
            sobran = len(palabra) - 8            
            if sobran == 1:
                print(f"\nLa palabra {palabra.upper()} tiene {len(palabra)} letras. \nSobra {sobran} letra.\n")                
            else:
                print(f"\nLa palabra {palabra.upper()} tiene {len(palabra)} letras. \nSobran {sobran} letras.\n")
        # elif para si el usuario introduce la palabra de salida se imprima un mensaje de salida.        
        elif palabra == "exit":
            print(f"Gracias por usar este programa. Hasta luego.\n")
            exit()
        # else por si llega a malir sal algo.
        else:
            print(f"Algo salió mal UwU.")
    except:
        break
