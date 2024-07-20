print(f"\nHola, este es un programa que te dice cuantas letras tiene la palabra que le escribas.\n\nSi quieres salir escribe la palabra exit.\n\n")

while True:
    try:
        palabra = input(str("Por favor introduce una palabra:"))
        if 3 < len(palabra) < 9 and palabra != "exit":
            print(f"\nLa palabra es {palabra} y tiene {len(palabra)} letras. Su longitud es correcta.\n")
        elif len(palabra) < 4:
            faltan = 4 - len(palabra) 
            if faltan == 1:
                print(f"\nLa palabra {palabra} solo tiene {len(palabra)} letras. \nFalta {faltan} letra.\n")                
            else:
                print(f"\nLa palabra {palabra} solo tiene {len(palabra)} letras. \nFaltan {faltan} letras.\n")             
        elif len(palabra) > 8:
            sobran = len(palabra) - 8            
            if sobran == 1:
                print(f"\nLa palabra {palabra} tiene {len(palabra)} letras. \nSobra {sobran} letra.\n")                
            else:
                print(f"\nLa palabra {palabra} tiene {len(palabra)} letras. \nSobran {sobran} letras.\n")
        elif palabra == "exit":
            print(f"Gracias por usar este programa. Hasta luego.\n")
            exit()
        else:
            print(f"Algo salió mal UwU.")
    except:
        break
