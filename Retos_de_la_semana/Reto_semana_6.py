# Programa que solicita una contraseña al usuario verifica que el primer caracter se un numero o de lo contrario le pide ingrese una nueva contraseña.
# No logre evitar que el programa continue si es que se usan simbolos tipo ".", "_", "#". "%", "/","$" al incio de la contraseña.
while True:
    try:
        # Se le pide al usuario ingresar una contraseña y use la funcion .isalpha para determinar si el primer caracter es alfabetico.
        password = (input("Ingresa una CONTRASEÑA:\n"))
        # Si el primer caracter es alfabetico pide al usuario que ingrese una nueva contraseña que incie con un numero.
        if password[0].isalpha():
            print(f"\nPor favor asegurate que tu CONTRASEÑA comience con un nÚmero.\n")
        else:
            break
    except ValueError:
        print(f"Algo salió mal uwu.")
# En este bloque de codigo se definen 3 intentos maximos para validar la contraseña
numero_de_intentos = 3
# Mientras el numero de intentos sea mayor que 0 seguira ejecutandose el bucle.
while numero_de_intentos > 0:
    # Se le pide al usuario que escriba de nuevo su contrasña.
    password_check = input(f"\nIntroduce de nuevo tu CONTRASEÑA:\n")
    # Se compara ambas contraseñas introducidas por el usuario. Si son iguales da un mensaje de conrtaseña correcta.
    if password == password_check:
        print(f"\nCONTRASEÑA correcta.\n\nHasta pronto.")
        exit()
    # Si las contraseñas no son iguales, da un mensaje pidiendole al usuario intentarlo de nuevo, y le menciona cuantos intentos le quedan.
    else:
        # Cada ejecucion incorrecta va reduciendo en uno en numero de intentos disponibles.
        numero_de_intentos -= 1
        if numero_de_intentos > 1:
            print(f"\nCONTRASEÑA incorrecta. Por favor intentalo otra vez.\nTe quedan {numero_de_intentos} intentos\n")
        elif numero_de_intentos == 1:
            print(f"\nCONTRASEÑA incorrecta. Por favor intentalo otra vez.\nTe queda {numero_de_intentos} intento\n")
        # Si se llegan a 0 intentos, se muestra un mensaje al usuario indicandole que ha excedido el numero de intentos y termina el programa.
        elif numero_de_intentos == 0:
            print(f"\nLas CONTRASEÑAS no coinciden.\n\nHas excedido el número de intentos.\n")
        else:  
            exit()