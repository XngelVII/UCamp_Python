import numpy as np
import matplotlib.pyplot as plt

# Se define la funcion de siluna la maquina de galton.
def maquina_de_galton(canicas, niveles):
    '''
    Esta funcion arroja tantas veces como numeros de canicas valores entre 0 y 1
    Durante ese proceso va sumando los 0 y 1 hasta cumplir el numero de niveles seteado
    Necesita de dos argumentos: El numero de canicas, y el numero de niveles que deberan de "caer"
    '''
    # Se define una lista vacia llamada resultados que tenga el numero de elementos igual al numero de niveles definidos
    # Cada uno de esos elementos representa los numeros desde el 0 hasta el numero de niveles definidos
    # En ocasiones me daba un error:
        #     Traceback (most recent call last):
        #   File "c:\Scripts\Ucamp\Simulacion_Maquina_de_Galton\Simulacion_Maquina_de_galton.py", line 66, in <module>
        #     main()
        #   File "c:\Scripts\Ucamp\Simulacion_Maquina_de_Galton\Simulacion_Maquina_de_galton.py", line 60, in main
        #     resultados = maquina_de_galton(canicas, niveles)
        #   File "c:\Scripts\Ucamp\Simulacion_Maquina_de_Galton\Simulacion_Maquina_de_galton.py", line 38, in maquina_de_galton
        #     resultados[posicion] += 1
        # IndexError: list index out of range
    # asi que tuve que incrementar el numero de niveles + 1 para garantizar durante la simulacion pudieran las canicas caer en un intervalo mayor al numero de caidas
    resultados = [0] * (niveles + 1)
    # print(f'tipo de resultados fuera del loop : \t{type(resultados)}')
    # En esta parte del codigo se hace la simulacion de la caida de las canicas
    # Se ejecuta un ciclo for para el numero de canicas 
    for i in range(canicas):
        # variable posicion que indica donde inician las canicas; cada que la canica cae un nivel la variavle posicion aumenta en 1 hasta el maximo de caidas definido
        posicion = 0
        # Se inicia un ciclo for para el numero de niveles (veces) que caeran las canicas
        for j in range(niveles):
            # La funcion np.random.randint(low=a, high=b) nos entrega un numero entero entre los numeros a y b 
            # https://www.geeksforgeeks.org/python-randint-function/
            # En esta parte del codigo con dicha funcion lo que hacemos es pedir que nos de aleatoriamente un 0 o un 1
            # Con cada caida se suma un 0 o un 1 a la variable posicion hasta que termina el numero de caidas
            # Al final de ciclo la variable deberia tener un valor entre 0 y el nivel de caidas (esta es la distribucion) p.e. 7
            posicion += np.random.randint(low=0, high=2)
            # print(f'Caida numero: {j+1}\n{posicion}') # lo use para ir viendo como iba cayendo cada canica con cada caida
        # print(f'Canica numero: {i+1}\n{posicion}') # lo use para ir viendo en a que numero llegaba la canica luego de todas las caidas
        # Se actualiza la lista de resultados sumandole uno a la posicion 
        # Se suman el numero de indicencias en las que las canicas cayeron en determinado valor (p.e. si cayeron 2 canicas en el 7)
        resultados[posicion] += 1
        # print(f'tipo de resultados:\n{resultados}') #Lo use para ir imprimiendo si iban creciendo los valores en cada caida
    return resultados

# Se define la funcion que imprime la grafica
def imprimir_grafica(resultados, niveles):
    '''
    Esta funcion imprime la grafica usando los valores obtenidos apartir de la funcion anterior
    Toma como argumentos los resultados de la caida de canicas de la funcion anterior ademas de los niveles que cayeron las canicas
    '''
    # Impresion de la grafica
    # Para configurar el tamaño de la grafica
    plt.figure(figsize=(9, 6))
    # Titulo de la grafica
    plt.title(f'Grafica de Canicas en la Maquina de Galton')
    # Etiqueta del eje x
    plt.xlabel('Contenedores')
    # Etiqueta del eje y
    plt.ylabel('Cantidad de Canicas')   
    # Para crear la grafica se usa como eje x el rango de comprende la longitud de los 'resultados' (cuantas veces cayeron las canicas), como el eje y los 'resultados' (cuantas canicas cayeron)
    plt.bar(range(len(resultados)), resultados, color='#3E74EF', linestyle='-')
    # Para configurar la cuadricula de la grafica: solo el eje Y tiene lineas de referencia, la linea es solida y el color gris.
    plt.grid(axis='y', linestyle='dotted', color='black')
    #Para mostrar la grafica
    plt.show()

def main():
    '''
    Esta es la funcion principal que llama a las funciones 'maquina de galton' e 'imprimir grafica'
    '''
    # Mensaje de bienvenida al usuario asi como peticion al usuario para ingresar los valores iniciales de canicas y niveles
    print('Hola, este es un programa que simula la Maquina de Galton y te muestra los resultados en una grafica.\n\nNota: De preferencia usa numeros no muy grandes la ejecucion tomara mas tiempo dependiendo de la potencia de tu computadora')
    while True:
        try:
            canicas = int(input('Cuantas canicas quieres simular?: '))
            niveles = int(input('Cuantas veces quieres que caigan?: '))
            # Si el usuario ingresa valores numericos enteros entonces continua con el siguiente bloque del codigo: Invocacion de funciones
            if isinstance(canicas, int) and isinstance(niveles, int):
                break
            else:
                print('Algo salio mal uwu')
        # Si el usuario ingresa un valor flotante o cadena de texto arroja un mensaje pidiendole que utilice solo numeros enteros
        except ValueError:
            print('Por favor ingresa números enteros.')
    # invoca a la funcion 'maquina de galton' usando los paramemetros de canicas y niveles luego enviandolo a la variable resultados
    resultados = maquina_de_galton(canicas, niveles)
    # invoca a la funcion 'imprimir grafica' usando los parametros resultados y niveles
    imprimir_grafica(resultados, niveles)

    print('\n\tGracias por usar este programa ✌️ n_n')

main()