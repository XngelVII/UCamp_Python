# Estructuras de datos que permiten almacenar y manipular conjuntos de datos
# Tipos principales: Listas, Tuplas, Conjuntos y Diccionarios
# Usos comunes: Manejo de datos, agrupacion de elementos, manipulacion de secuencias

# Listas
# Sintaxis: mi_lista = [1, 2, 3, 'a', 'b', 'c']
# Operaciones comunes 
# Accesso mi_lista[0]
# Adicion mi_lista.append('d')
# Eliminacion mi_lista.remove(1)
# Segmentar mi_lista[1:4]

mi_lista = [1,2,3,4,5]
print(f"esta es mi_lista {mi_lista}")
print("metodo 1 para agregar nuevos elementos a la lista \nmi_lista.append(6)")
mi_lista.append(6)
print(mi_lista)
print("metodo 2 para agregar nuevos elementos a la lista \nmi_lista = mi_lista + [7,8]")
mi_lista = mi_lista + [7,8]
print(mi_lista)

tamano_de_lista = len(mi_lista)
print(f"Tamaño de lista: {tamano_de_lista}")
print("Ejercicio para sumar elementos en una lista")
print("Para acceder a elementos de una lista por indice debemos definir un rango")
print("Rango de numeros:")

intervalo = range(0,tamano_de_lista)
print(list(intervalo))

print("inicio de ciclo")
for index in intervalo:
    print(f"\tvalor del indice [{index}]: {mi_lista[index]}")
    print(f"\t sumar 10 a {mi_lista[index]} a nuestra lista")
    mi_lista[index] = 10 + mi_lista[index]
    print(f"\t  nuevo valor dek indice [{index}] es: {mi_lista[index]}")
print(f"El nuevo valor de mi_lista es:\n{mi_lista}")

# Tuplas
# Sintaxis: mi_tupla = (1, 2, 3, 'a', 'b', 'c')
# Caracteristicas:    Inmutabilidad (no se pueden modificar despues de ser definidas)
#                     Uso en estructuras constantes y para desempaquetar

print("\n\n\nComo consultar elementos de una tupla:")
coordenadas = (89,69)
print(f"{coordenadas}")
print(f"{coordenadas[0]}")


# Conjuntos
# Sintaxis: mi_conjunto = {1, 2, 3, 'a', 'b', 'c'}
# Adicion mi_conjunto.append('d')
# Eliminacion mi_conjunto.remove(1)
# Operaciones de conjuntos: Union (|), Interseccion (&), Diferencia (-)

print("\n\n\nEjercicio de conjuntos\n")
set_a = {1,2,3,5,"a"}
set_b = {5,6,7,8,9,"c"}
set_c = {"a","b","c","d",5}
set_d = {1,9,"e","a"}

print(f"Conjunto a:\n{set_a}\nConjunto b:\n{set_b}\nConjunto c:\n{set_c}\nConjunto d:\n{set_d}\n")

print(f"Union entre conjuntos a,b,c,d: \n{ set_a | set_b | set_c | set_d }")
print(f"Interseccion entre conjuntos a,b (solo funciona con dos conjuntos): \n{ set_a & set_d }")
print(f"Diferencia conjuntos a,b,c,d: \n{ set_a - set_b - set_c - set_d }")

lista_repetida = [1,1,1,1,1,1,2,2,2,2,5,5,5,5,5,5]
print(f"\n\nElementos de la lista_repetida:\n{lista_repetida}\n\nConjunto de elementos unicos en la lista_repetida:\n{set(lista_repetida)}")


# Diccionarios
# Sintaxis: mi_diccionario = {'clave1' : 'valor1', 'clave2' : 'valor2'}
# Acceso mi_diccionario['clave1']
# Adicion/modificacion mi_diccionario['clave3'] = 'valor3'
# Eliminacion del mi_diccionario['clave1']