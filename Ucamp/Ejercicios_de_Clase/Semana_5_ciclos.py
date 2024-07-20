
# iteracion for
# for i in range (0,20):
#     print(f'iterador',i )

# for j in [1,2,3,4,5,6,7,8,9]:
#     print('\n numero',j)


# iteracion while 
# i = 0
# while i < 10:
#     print(i)
#     i += 1


# declaracion break, sirve para romper la ejecucion. fuciona con while, for, if elif, y hasta elses
# for letra in 'Python':
#     if letra == 'h':
#         break
#     print(f"letra actual:{letra}")

# declaracion continue. Se salta el paso si se cumple la condicional, pero continua la ejecuacion del programa
# for letra in "Python":
#     if letra == "h":
#         continue
#     print(f"letra actual {letra}")


# Juego adivinador
import random

lista_nombres = ["drak","klk","kvn","chamo","dogman","angel"]
nombre_ganador = random.choice(lista_nombres)

numero_de_intentos = 3

while numero_de_intentos > 0:
    print(f"intentos restantes: {numero_de_intentos}")
    resultado = input("dime en quien de kaoos estoy pensando:")
    if resultado == nombre_ganador:
        print("EZ WIN")
        break
    else:
        print(f"try harder")
    numero_de_intentos -= 1
print(f"GG")

