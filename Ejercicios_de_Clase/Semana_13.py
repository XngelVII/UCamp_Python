# # Cuando ejecutamos codigo a veces podemos cometer errores en la logica dle programa, o en el resultado que estamos esperando.
# # Usualmente estos errores ocasionan la terminacion del programa

# # ValueError: ocurre cuando una funcion recibe un argumento de tipo correcto pero con un valor inapropiado
# # TypeError se produce cuando una operacion o funcion es aplicada a un obejto de tipo inapropiado
# # AttributeError se lanza cuando un objeto no tiene un atributo o metodo especifico
# # IndentationError sucede cuando la identacion del codigo no es correcta
# # NameError ocurre cuando de intenta usar una variable o funcion que no esta definida
# # ZeroDivisionError se produce cuando se intenta dividir un numero por cero
# # IndexError sucede cuando se intenta acceder a un indice que esta fuera del rango de una lista o secuencia 
# # KeyError se lanza cuando se intenta acceder a una clave en un diccionario que no FileExistsError

# # Clausulas try/except
# # Se pueden usar varias excepciones 
# # Bloque else para ejecutar codigo si no ocurre una excepcion
# # bloque finally para codigo que siempre debe ejecutarse

# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("Error: Division por cero.")
# except ValueError:
#     print("Error: Valor no valido.")
# else:
#     print(f"El resultado es: {result}")
# finally:
#     print("Este bloque se ejecuta siempre.")


# def error_identacion():
#     try:
#         exec("""
#     def mal_indent():
#     print('Hola)
# """)
#     except IndentationError:
#         print('Ocurrio un error de identacion en la funcion dada')


def menu_display():
    print('Programa de calificaciones:')
    print('1) Agregar nombres a una lista')
    print('2) Asignar calificaciones a un nombre')
    print('3) Imprimir toda la informacion')
    opcion = float(input('Ingrese la opcion que desees realizar: '))
    try:
        opcion = opcion / 1
        if opcion == 1:
            print('Subrutina de agregar nombres')
        elif opcion == 2:
            print('Subrutina para signar calificacion')
        elif opcion == 3:
            print('Subrutina para signar calificaciones')
    except ValueError:
        print('Error de valor')
    except TypeError:
        print('Error de valor')

menu_display()