colores_eng = {'Red': 'Rojo','Orange': 'Naranja', 'Yellow': 'Amarillo', 'Green': 'Verde', 'Blue': 'Azul', 'Indigo': 'Indigo', 'Purple': 'Morado', 'Brown': 'Cafe', 'Cyan': 'Aquamarina', 'Pink': 'Rosa', 'Violet': 'Violeta'}
colores_esp = {'Rojo': 'Red', 'Naranja': 'Orange', 'Amarillo': 'Yellow', 'Verde': 'Green', 'Azul': 'Blue', 'Indigo': 'Indigo', 'Morado': 'Purple', 'Cafe': 'Brown', 'Aquamarina': 'Cyan', 'Rosa': 'Pink', 'Violeta': 'Violet'}

while True:
    try:
        opcion = input('Por favor selecciona un idioma (Please choose a lenguage):\t\n(1) Español\t\n(2) English\n')
        if opcion != '1' and opcion != '2':
            print(f'Por favor ingresa una opcion valida')
        else:
            break
    except ValueError:
        print(f"Algo salió mal uwu.")

if opcion == '1':
    frase = input('Por favor ingresa un color en español: ')
    frase = frase.capitalize()
    color = frase.split()
    respuesta = ''
    for palabra in color:
        if palabra in colores_esp:
            respuesta += 'Asi se dice ' + frase.upper() + ' en ingles: \n' + colores_esp[palabra]
        else:
            respuesta += 'Creo que no sé cómo se traduce al inglés el color ' + palabra
    print(f'{respuesta}\n\nAdios...n_n')
elif opcion == '2':
    frase = input('Please enter a color in english: ')
    frase = frase.capitalize()
    color = frase.split()
    respuesta = ''
    for palabra in color:
        if palabra in colores_eng:
            respuesta += 'This is how you say ' + frase.upper() + ' in spanish: \n' + colores_eng[palabra]
        else:
            respuesta += "I'm not sure how to traduce the color " + palabra + " to spanish"
    print(f'{respuesta}\n\nGood bye... n_n')


