# Al iniciar el programa, se mostrará un menú con las siguientes opciones:
#   Agregar un nuevo alumno (1).
#   Ver los alumnos y las calificaciones (2).
#   Salir (S).
# Si se decide agregar un nuevo alumno, corroborar que el nombre no esté en blanco.
# Preguntar cuántas calificaciones se quiere agregar.
# Si se ingresa una calificación que no sea de tipo numérico, se pedirá volver a intentar.
# Después de agregar la información de un alumno, volver al menú principal.
# Si se selecciona la opción 2, mostrar en la pantalla la información de cada alumno y el promedio de sus calificaciones. Ejemplo: “Laura Ramírez: Promedio 9.5”
# Si se selecciona la opción ‘S’, indicar que se cerrará el programa y preguntar si se está seguro de cerrar el programa o no. 
# Recuerda que lo más importante es que nodeberá detenerse la ejecución del programaen caso de ingresar valores equivocados.

# Se define una lista de alumnos vacias donde se iran agregando la informacion de los alumnos
lista_de_alum = []

# Funcion para agregar un alumno 
def agregar_alumno():
    '''
    Esta funcion pide al usuario agregar apellido, nombre, cuantas calificaciones asi como el valor de cada una de esas calificaciones
    Agrega las calificaciones a una lista
    Agrega los nombres, apellidos y lista de calificaciones a un diccionario
    '''
    apellido = input('Ingresa el apellido del alumno: ')
    apellido = apellido.upper()
    # Si appellido esta escrito con caracteres alfabeticos continua
    if apellido.isalpha():
        nombre = input('Ingresa el nombre del alumno: ')
        nombre = nombre.upper()
        # Si nombre esta escrito con caracteres alfabeticos continua
        if nombre.isalpha():
            try:
                # Se preguntan cuantas materias se quieren ingresar
                materias = int(input('¿Cuántas calificaciones vas a ingresar?: '))
            except ValueError:
                # Si el valor no es un numero entero lanza un mensaje de error
                print('Por favor ingresa un número válido de materias.\n')
                return agregar_alumno()
            # Definir una una lista que almacenara la calificaciones del alumno
            calif_alum = []
            # Ciclo for que por cada elemento hasta el numero total de materias pedira introducir una calificacion
            # Y Agregara la calificacion a la lista de calificaciones
            for i in range(materias):
                try:
                    calificacion = float(input('Ingrese una calificación: '))
                    calif_alum.append(calificacion)
                # Except para garantizar que el usuario ingrese valores correctos
                except ValueError:
                    print('Debe ingresar un valor numérico correcto.\n')
            # Se define un diccionario y se agregan los valores de apellido, nombre y la lista de calificaciones para cada alumno
            lista_de_alum.append({'nombre': nombre, 'apellido': apellido, 'calificaciones': calif_alum})
            return nombre, calif_alum
        # Si no se ingresa un nombre correcto se regresa al inicio de la funcion
        else:
            print('Por favor ingresa un nombre correcto.\n')
            return agregar_alumno()
    # Si no se ingresa un apellido correcto se regresa al inicio de la funcion
    else:
        print('Por favor ingresa un apellido correcto.\n')
        return agregar_alumno()
    return {'nombre': nombre, 'apellido' : apellido, 'calificaciones' : calif_alum}

# Funcion para calcular el promedio
def calcular_promedio(calificaciones):
    '''
    Esta funcion calcula el promedio de las calificiones de los alumnos
    Necesita como parametros las calificaciones contenudas en la lista de calificaciones 'calif_alum'
    '''
    return sum(calificaciones) / len(calificaciones)

# Funcion para mostrar alumnos 
def mostrar_alumnos():
    '''
    Funcion que muestra muestra los alumnos y su promedio
    Para cada alumno en la lista de alumnos llama a la funcion calcular promedio 
    Imprime en pantalla los nombres apellidos asi como los resultados que arroja la funcion calcular promedio
    '''
    # Puse un condicional porque de otro modo si el usuario iniciaba el programa y queria ver los alumnos daba error
    # Si la lista de alumno no esta vacia imprime los datos del alumno
    if lista_de_alum:
        for alumno in lista_de_alum:
            promedio = calcular_promedio(alumno['calificaciones'])
            print(f'{alumno["nombre"]} {alumno["apellido"]}\nPromedio: {promedio:.2f}\n----------------------------------------')
        #Si la lista de alumnos esta vacia entonces muestra un mensaje pidiendole al usuario que agrege un usuario primero y llama a la funcion main
    else:
        print('Por favor primero ingresa un alumno.\n')
        main()

# Funcion guardar alumnos 
def guardar_alumnos():
    '''
    Esta funcion sirve para guardar los nombres u el promedio de los alumnos en un archivo de texto
    '''
    # Use el mismo condicional para que si el usuario no pueda guardar el archivo hasta que se ingrese al menos un alumno
    # Con un with/as  se guarda la informacion recolectada por als funciones calcular_promedio y agregar_alumno
    if lista_de_alum:
        with open('Calificaciones_de_alumnos.txt', 'w') as f_lista:
            for alumno in lista_de_alum:
                promedio = calcular_promedio(alumno["calificaciones"])
                # Use el mismo formato de la funcion mostrar_alumnos que guardar la informacion
                f_lista.write(f'{alumno["nombre"]} {alumno["apellido"]}\nPromedio: {promedio:.2f}\n----------------------------------------\n')
        print('Datos guardados en Calificaciones_de_alumnos.txt\n')
    else:
        print('Por favor primero ingresa un alumno.\n')
        main()


#Funcion principal
def main():
    '''
    Funcion principal que saluda al usuario y le presenta 3 opciones
    1 Ingresar alumno
    2 Mostrar alumnos
    3 Salir
    dependiendo de la opcion ingresada por el usuario llamara a las otras funciones o sale del programa
    '''
    while True:
        try:
            # Saluda al usuario y le presenta 3 opciones y entra en un condicional dependiendo de la entrada del usuario.
            # La opcion .upper al final fue para garantizar que aunque el usuario escriba s o S pueda salir de programa
            opcion = input('Hola, por favor ingresa una opción:\n\t(1) Agregar un nuevo alumno.\n\t(2) Ver los alumnos y las calificaciones.\n\t(3) Guardar calificaciones.\n\t(S) Salir.\n----------------------------------------\n\t').upper()
            if opcion == '1':
                agregar_alumno()
            elif opcion == '2':
                mostrar_alumnos()
            elif opcion == '3':
                guardar_alumnos()
            # Agregue un if para que si el usuario escoge la opcion salir se le pregunte si desea guardar y salir, cancelar, o salir (sin guardar)
            elif opcion == 'S':
                exit_opcion = input('Quieres guardar antes de salir?:\n\t(1) Guardar y salir.\n\t(2) Cancelar.\n\t(3) Salir.\n----------------------------------------\n\t')
                if exit_opcion == '1':
                    guardar_alumnos()
                    print('Hasta luego.')
                    exit()
                elif exit_opcion == '2':
                    main()
                elif exit_opcion == '3':
                    print('Hasta luego.')
                    exit()
                else:
                    print('Por favor escoge una opción válida.\n')
                    main()
            else:
                print('Por favor escoge una opción válida.\n')
        except ValueError:
            print('Si estás leyendo esto, algo salió muy mal.')

main()