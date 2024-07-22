# Creacion de listas vacias que contendran los nombres y las calificaciones de los alumnos
# Aunque se podrian agregar todos los datos a una sola lista (nombre y calificaciones) tuve problemas para sacar el promedio ya que esa lista tendria datos numericos y cadenas de texto
# Asi que opte por en una lista poner solo los nombres (str) y en otra las calificaciones (int)
lista = []
calificaciones = []
# Definicion de la variable alumnos igual a cero como valor inicial
alumnos = 0
# Bloque de codigo para ingreso de informacion
# El programa acepta hasta 30 alumnos con sus respectivos nombres y califaciones
# Mientras el numero de alumnos sea menor a 30 seguira ejecutandose con normalidad
while alumnos < 30:
    try:
        # Se le pregunta al usuario qué quiere hacer dandole 2 opciones
        opcion = input(f'Hola Usuario, por favor usa una de las siguientes opciones:\n\t(1) Agregar un alumno\n\t(0) Salir\t\n')
        # Si el usuario escoge la opcion 1 entonces se le pide que ingrese el nombre y 5 calificaciones del alumno en cuestion
        if opcion == '1':
            # Se usa la funcion .capitalize() para que el nombre se guarde con una mayuscula inicial
            nombre = input(f'Ingresa el nombre del alumno: ').capitalize()
            # If para garantizar que el nombre este conformado por caracteres alfabeticos
            if nombre.isalpha():
                # Peticion de las calificaciones del alumno
                calificacion_1 = float(input(f'Ingresa la calificacion de {nombre}: '))
                calificacion_2 = float(input(f'Ingresa la calificacion de {nombre}: '))
                calificacion_3 = float(input(f'Ingresa la calificacion de {nombre}: '))
                calificacion_4 = float(input(f'Ingresa la calificacion de {nombre}: '))
                calificacion_5 = float(input(f'Ingresa la calificacion de {nombre}: '))
                # Se agrega el nombre del alumno a la lista 
                lista.append(nombre)
                # Se agregan las calificaciones a una lista llamada calif_materias que posteriormente se agregan a la lista de calificaciones
                calif_materias = [calificacion_1,calificacion_2,calificacion_3,calificacion_4,calificacion_5]
                calificaciones.append(calif_materias)
                # Se incrementa por uno el numero de alumnos
                alumnos += 1
            else:
                # Si el usuario ingresa un nombre que tenga numeros se mostrara el siguiente comentario y regresara al bloque de codigo anterior
                print(f'{nombre} es un nombre inválido. No uses numeros.')
                continue
        # Si el usuario escoge la opcion 0 entonces terminara la ejecucion de este bloque de codigo e ira hasta el bloque donde se calculan e imprimen los resultados
        elif opcion == '0':
            break
        # si el usuario no escoge las opciones dada (1 o 0) se mostrara el siguiente mensaje y volvera con el bloque anterior de codigo
        else:
            print('Haz ingresado una opcion invalida')
            continue
    # Si el usuario no coloca un numero en las calificaciones se mostrara el siguiente comentario y volvera al bloque de codigo anterior
    except ValueError:
        print(f"Por favor ingresa una calificacion")
        continue
# Se crea una nueva lista donde se guardaran los promedios de los alumnos
promedios = []
# Bloque de codigo para calcular e imprimir los resultados
# Para cada elemento en el rango de la lista de alumnos: se calculara el promedio y luego ese valor se agregara a la lista promedio
for i in range(len(lista)):
    # Encontre la funcion sum() que suma todos los elementos de una lista siempre y cuando sean elementos numericos
    # Para calcular el promedio se suman los valores de la calificacion de cada materia y se dividen entre el numero de materias
    # En este caso sum() / len()
    promedio_alumno = sum(calificaciones[i]) / len(calificaciones[i])
    # Se agrega el valor del promedio_alumno a la lista de promedios
    promedios.append(promedio_alumno)
    # Impresión de las calificaciones de cada alumno
    print(f'\nLas calificaciones del alumno {lista[i]} son: {calificaciones[i]}')
    # Impresion del promedio de cada alumno. La opcion :.2f significa que solo va a mostrar dos digitos luego del punto decimal
    print(f'Su promedio para este periodo es: {promedios[i]:.2f}')
# Mensaje de despedida para el usuario
print(f'\n\tGracias por usar este programa.\n\t\tHasta luego.\n')