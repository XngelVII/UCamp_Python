lista = []

for numero in range(10):
    numero = numero**2
    lista.append(numero)
print(f'{lista}\n{numero}')

cuadrados = [cuad **2 for cuad in range(10)]
print(cuadrados)

cubos = [cubo **3 for cubo in range(10)]
print(cubos)

###############################################
crear un diccionario por medio de la compresion de listas

# Cuadrados
cuad = {numero_c: numero_c **2 for numero_c in range(10)}
print(f'{cuad}')

# Cubos
cubos = {numero: numero **3 for numero in range(10)}
print(f'{cubos}')


pares = [numero for numero in range(1,11) if numero % 2 == 0]
print(pares)
impares =  [numero for numero in range (1, 11) if numero % 2 ==1]
print(impares)

nombres = ['ale','kvn','trufa','santos','miguel']
print(f'lista antes de la compresion:\n{nombres}')
nombres = [nombre.capitalize() for nombre in nombres]
print(f'lista despues de la compresion:\n{nombres}')