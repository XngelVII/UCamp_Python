# Saludo al usuario y da una breve descripción del programa
print(f"Hola, soy un programa que te ayuda calcular los años que han pasado entre 2 años\n")

#  While que menciona que mientras sea verdad que el año actual es menor que cero o que la longitud de la variable actual_year_count es diferente de 4 digitos lanzara mensaje de error.
while True:
    try:
        # Mensaje pidiendo el año acual al usuario.
        actual_year = int(input(f"Por favor ingresa el año actual (YYYY): "))
        # Asignando a una nueva variable str la anterior variable int
        actual_year_count = str(actual_year)
        # Si la variable int es menor a cero o la longitud de la variable str es diferente de 4 manda un mensaje para solicitarle al usuario ingrese un numero válido.
        if actual_year <= 0 or len(actual_year_count) != 4:
            print(f"Por favor ingresa un año válido. Con cuatro digitos (YYYY)\n")
        else:
            break
    # Si el usuario ingresa letras o simbolos enviara un mensaje.
    except ValueError:
            print(f"Por favor no uses letras o simbolos\n")

#  While que menciona que mientras sea verdad que el año actual es menor que cero o que la longitud de la variable actual_year_count es diferente de 4 digitos lanzara mensaje de error.
while True:
    try:
        # Mensaje pidiendo el año final al usuario.
        year_final = int(input(f"Por favor ingresa el año final (YYYY): "))
        # Asignando a una nueva variable str la anterior variable int
        year_final_count = str(year_final)
        # Si la variable es menor a cero o la longitud es diferente de 4 manda un mensaje para solicitarle al usuario ingrese un numero válido.
        if year_final <= 0 or len(year_final_count) != 4:
            print(f"Por favor ingresa un año válido. Con cuatro digitos (YYYY)\n")
        else:
            break
    # Si el usuario ingresa letras o simbolos enviara un mensaje.
    except ValueError:
            print(f"Por favor no uses letras o simbolos\n")
# Bloque condicional que lanza mensajes dependiendo de si las variables actual_year y year_final son iguales, mayores que o menores que
if actual_year == year_final:
    print(f"\nIngresaste el mismo año en ambos campos, estamos en {actual_year}")
elif actual_year > year_final and actual_year - 1 != year_final:
    pasado = (year_final - actual_year) * -1
    print(f"\nHan pasado {pasado} años entre {year_final} y {actual_year}.")
elif actual_year < year_final and actual_year + 1 != year_final:
    futuro = (year_final - actual_year)
    print(f"\nYa que estamos en {actual_year} faltan {futuro} años para llegar al {year_final}.")
elif actual_year > year_final and actual_year - 1 == year_final:
    pasado_2 = (year_final - actual_year) * -1
    print(f"\nHa pasado {pasado_2} año entre {year_final} y {actual_year}.")
elif actual_year < year_final and actual_year + 1 == year_final:
    futuro_2 = year_final - actual_year
    print(f"\nYa que estamos en {actual_year} falta {futuro_2} año para llegar al {year_final}.")
else:
    print(f"\nsomething went wrong \nu_u\n )")
