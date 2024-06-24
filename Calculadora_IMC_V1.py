# Saludar y solicitar al usuario su nombre (definir variables de cadenas de texto)
print(f"Hola soy una calculadora de Indice de Masa Corporal (IMC).")
nombre = str(input("Por favor dime cuál es tu nombre: "))
nombre = nombre.capitalize()
apellido_paterno = str(input("Dime cuál es tu apellido paterno: "))
apellido_materno = str(input("¿Y tu apellido materno?: "))

# Preguntar la edad del usuario (definir variables de valores numericos)
edad = int(input("¿Cuántos años tienes?: "))

print(f"Excelente {nombre}, ahora necesito que por favor me brindes un par más de datos: ")

# Solicitar al usuario su peso y altura (definir variables de punto flotante)
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

# Calcular el IMC del usuario
imc = float(peso/altura**2) 

# Imprimir el resultado del calculo del IMC
print(f"Muy bien {nombre} tu IMC es: {imc : .2f}")

if imc < 16:
    print(f"Estás dentro de la clasificación de DELGADEZ SEVERA")
elif 16.0 <= imc <= 16.999999:
    print(f"Estás dentro de la clasificación de DELGADEZ MODERADA")
elif 17.0 <= imc <= 18.4999999:
    print(f"Estás dentro de la clasificación de DELGADEZ LEVE")
elif 18.5 <= imc <= 24.999999:
    print(f"Estás dentro de la clasificación de NÓRMAL")
elif 25.0 <= imc <= 29.999999:
    print(f"Estás dentro de la clasificación de PRE OBESIDAD")
elif 30.0 <= imc <= 34.999999:
    print(f"Estás dentro de la clasificación de OBESIDAD LEVE")
elif 35.0 <= imc <= 39.999999:
    print(f"Estás dentro de la clasificación de OBESIDAD MODERADA")
elif imc > 40.0:
    print(f"Estás dentro de la clasificación de OBESIDAD MORBIDA")
