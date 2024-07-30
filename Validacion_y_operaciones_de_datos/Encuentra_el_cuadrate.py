# Mensaje de bienvenida al usuario
print(f"Hola, te ayudaré a saber en qué cuadrante se encuentran las coordenadas que me indiques\n\nPara salir ingresa los valores x = 0.1 y y = 0.1")

# while para que mientras "x" y "y" sean variables flotantes se ejecuten las condicionales.
# Agregué un  en cada condicional ya que de otra manera el programa se iniciaba recursivamente luego de dar un primer resultado (pedia de nuevo valores para "x" y "y", daba un resultado y se reiniciaba)
while True:
    try:
        # Peticion al usuario de variables "x", "y" y asignacion a tipo flotante para que se acepten numeros con decimales
        x = float(input("Por favor ingresa el valor de X: "))
        y = float(input("Por favor ingresa el valor de Y: "))
        # Condicional para determinar si las variables son de tipo flotante o no. Si son flotantes se ejecutaran las siguientes conficionales. Si no son flotantes se mandara mensaje de exepcion
        if isinstance(x, float) and isinstance(y, float):
            # Condicional para determinar si el punto esta en el origen cartesiano
            if x == 0 and y == 0:
                print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Origen Cartesiano")
            # Condicional para determinar si el punto esta en el eje y
            elif x == 0: 
                print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Eje Y")
            # Condicional para determinar si el punto esta en el eje x
            elif y == 0:
                print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Eje X")
            # Condicional para determinar si el punto esta en el cuadrante 1 con "x" y "y" ambas positivas
            elif x > 0 and y > 0 and x != 0.1 and y != 0.1:
                print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Cuadrante 1")
            # Condicional para determinar si el punto esta en el cuadrante 3 con "x" y "y" ambas negativas
            elif x < 0 and y < 0:
                print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Cuadrante 3")
            # Condicional para determinar si el punto esta en el cuadrante 2 con "x" positiva y "y" negativa
            elif x > 0 and y < 0 and x != 0.1 :
                print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Cuadrante 2")
            # Condicional para determinar si el punto esta en el cuadrante 2 con "x" negativa y "y" positiva
            elif x < 0 and y > 0 and y != x != 0.1:
                print (f"El Punto para las coordenadas que proporcionaste se encuentra en el Cuadrante 4")  
            elif x == 0.1 and y == 0.1:
                print(f"\n\nGracias por usar este programa.\n\nPor cierto esos valores estan en el Cuadrante 1.\n\nHasta pronto.")
                exit()
            else:
                print(f"Algo salió mal u_u.")
    except ValueError:
        print(f"Por favor ingresa un números. No uses letras o símbolos.")