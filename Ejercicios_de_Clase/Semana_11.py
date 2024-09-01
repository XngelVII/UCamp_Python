import matplotlib.pyplot as plt
import numpy as np

# array1 = np.array([1,5,10])
# print(f'array1: {array1}')
# #print(type(array1))
# array2 = np.array([6,1,7])
# print(f'array2: {array2}')
# #print(type(array2))
# # Se suman elementos (n + n) de los arrays
# print(f'Suma de array1 + array2 {array1 + array2}')
# print(f'Resta de array1 - array2 {array1 - array2}')
# print(f'multiplicacion de array1 * array2 {array1 * array2}')

# print(f'Raiz cuadrada de array1 {np.sqrt(array1)}:')

# print(f'media (promedio) cuadrada de array1 {np.mean(array1)}:')

# print(f'mediana de array1 {np.median(array1)}:')

# print(f'distribucion estandar de array1 {np.std(array1)}:')

# 1.- Crear un arreglo de numpy con datos de x

lista_num = [0.4,12.15,10,2.3,-9.999,0,5.23,8.65,7.7]

X = np.array(lista_num)

# 2.- Crear una funcion para una variable y 

# f(x) = y
def f(x):
    '''
    Devuelve una funcion de tipo
    y = a*x**2 + b*x + c
    '''
    a = 2
    b = 1
    c = 3
    return (a * (x ** 2) + b * x + c)

Y = f(X)

# 3.- Crear un grafico

plt.scatter(x=X,y=Y)
plt.show()