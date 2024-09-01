import numpy as np
import matplotlib.pyplot as plt

# distribucion normal
# simetria la distribucion es simetrica respecto a la media
# Media mediana y moda todos coinciden en el mismo punto
# distribucion: aproximadamente el 68% de los datos estan dentro de una desviacion estandar de la media

# data = np.random.normal(loc=0, scale=1, size=10)
# print(data)

# data2 = np.random.rand()
# print(data2)

# data3 = np.random.randint(1)
# print(data3)

# # bins: ajustar el numero d eintervalos para obtener mas detalle o mayor generalizacion
# #     ejemplo: bins=10 vs bins=50
# # colores: usar diferentes colores para representar mejor los datos
# #     ejemplo: color='blue' vs color='red' 
# # estilos de bordes: añadir bordes a las barras para mayor claridad
# #     ejemplo: edgecolor='black'

# plt.hist(data, bins=30, color='blue', edgecolor='black')
# plt.title('Histograma de distribucion normal')
# plt.xlabel('valor')
# plt.ylabel('frecuencia')
# plt.show()

# generacion de numeros aleatorios
# todas se encuentran dentro de un submodulo
np.random.rand() # genera numeros aleatorios de 0 a 1 pero no los hace de forma distribucion normal
np.random.randn() # genera numeros aleatorios con una media en 0 y desviacion std en 1 (estos si son distribucion normales y estandar)

data4 = np.random.normal(
    loc=0, # el valor correspondiente a la media
    scale= 1, # el valor correspondiente a la desviacion std
    size= 3000 # el numero de datos que deseamos generar
)

# los datos se van a guardar en la variable data4

# Generacion de histogramas

# esto se hace en maplotlib.pyplot con el medoto hist()

plt.hist(x= data4, bins = 12)
# arreglos de titulos y etiquetas en ejes
plt.title('Implementacion de maquina de galton')
plt.xlabel('valor')
plt.ylabel('frecuencia')
# mostrar el grafico
plt.show()