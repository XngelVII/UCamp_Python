# Mensaje de bienvenida al usuario
print(f"Hola, te ayudaré a saber en qué cuadrante se encuentran las coordenadas que me indiques\n")

# while con opciones para que el usuario pueda escoger si indtroduce coordenadas o sale del programa
while True:
    try:
        opcion = input('Escoge una opcion:\n(1) Ingresar coordenadas.\n(2) Salir.\n')
        if opcion != '1' and opcion != '2':
            print('\nPor favor escoge una opcion correcta.\n')
        elif opcion == '1':
        # Peticion al usuario de variables "x", "y" y asignacion a tipo flotante para que se acepten numeros con decimales
            x = float(input("Por favor ingresa el valor de X: "))
            y = float(input("Por favor ingresa el valor de Y: "))
            # Condicional para determinar si las variables son de tipo flotante o no. Si son flotantes se ejecutaran las siguientes conficionales. Si no son flotantes se mandara mensaje de exepcion
            if isinstance(x, float) and isinstance(y, float):
                # Condicional para determinar si el punto esta en el origen cartesiano
                if x == 0 and y == 0:
                    print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Origen Cartesiano.\n")
                # Condicional para determinar si el punto esta en el eje y
                elif x == 0: 
                    print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Eje Y.\n")
                # Condicional para determinar si el punto esta en el eje x
                elif y == 0:
                    print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Eje X.\n")
                # Condicional para determinar si el punto esta en el cuadrante 1 con "x" y "y" ambas positivas
                elif x > 0 and y > 0:
                    print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Cuadrante 1.\n")
                # Condicional para determinar si el punto esta en el cuadrante 3 con "x" y "y" ambas negativas
                elif x < 0 and y < 0:
                    print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Cuadrante 3.\n")
                # Condicional para determinar si el punto esta en el cuadrante 2 con "x" positiva y "y" negativa
                elif x > 0 and y < 0:
                    print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Cuadrante 2.\n")
                # Condicional para determinar si el punto esta en el cuadrante 2 con "x" negativa y "y" positiva
                elif x < 0 and y > 0:
                    print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Cuadrante 4.\n")
                else:
                    print(f"Algo salió mal u_u.\n")
        elif opcion == '2':
            # Mensaje de salida
            print(f"\nGracias por usar este programa.\n\nHasta pronto.\n")
            exit()
    except ValueError:
        print('Algo sallio mal uwu\n')
