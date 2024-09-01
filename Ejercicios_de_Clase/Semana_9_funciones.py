# Definicion de un diccionario con todas las letras
alfa = {
"a" : 0,
"b" : 1,
"c" : 2,
"d" : 3
}

print(alfa)

print('Seleccion por clave')
print(alfa["a"])
print('Seleccion por llaves')
print(alfa.keys())
print('Seleccion por elementos (muestra llaves y valores)')
print(alfa.items())
print('Seleccion por valores')
print(alfa.values())






# Una Función es un bloque de cópdigo que realiza una tera especifica y puede ser reutilizado en diferentes partes de un programa
# -reutilizacion de codigo
# -modularidad y irganizacion
# -mantenimiento mas sencillo


# Parametros: Variables en la definicion de la funcion.
# Argumentos: Valores pasados a la funcion cuando se llama.
# Tipos de argumentos 
#     posicionales
#     por palabra clave
#     por defecto
#     *args (Argumentos variables)
#     **kwargs (argumentos con palabras clave variables)


# Funciones

# def nombre_de_la_funcion(parametros):
#     '''Documentacion de la funcion'''
#     Instrucciones
#     return valor_de_retorno


# def saludo():
#     print('Hola')

# def saludo_documentacion():
#     """"Imprime un saludo"""
#     print('Hola')


# # Para llamar la funcion:
# saludo()


# def saludo_parametro(nombre):
#     """"Imprime un saludo"""
#     print('Hola' , nombre)


# saludo_parametro(nombre='Miguel')

# def saludo_completo(nombre, apellido):
#     """"Imprime un saludo"""
#     print('Hola' ,  nombre , '' , apellido)

# saludo_completo(nombre='Miguel', apellido='Tapia')


# def saludo_generico(nombre='mundo'):
#     """"Imprime un saludo"""
#     print('Hola' ,  nombre)


# saludo_generico()
# saludo_generico('Miguel')

# Saludo alreves

def saludo_al_reves(nombre='mundo'):
    cadena_invertida = ''
    for char in nombre:
        cadena_invertida = char + cadena_invertida
    return cadena_invertida

def mayusculas(palabra):
    print(palabra.upper())

linea =  saludo_al_reves('Hola querido usuario')
print(linea)
mayusculas(linea)