# Saludar y solicitar al usuario su nombre (definir variables de cadenas de texto)
print(f"Hola soy una calculadora de Indice de Masa Corporal (IMC).")
nombre = str(input("Por favor dime cuál es tu nombre: "))
nombre = nombre.capitalize()
apellido_paterno = str(input("Dime cuál es tu apellido paterno: "))
apellido_paterno = apellido_paterno.capitalize()
apellido_materno = str(input("¿Y tu apellido materno?: "))
apellido_materno = apellido_materno.capitalize()

# Preguntar la edad del usuario (definir variables de valores numericos)
# Agregué un while / try para confirmar que el usuario ingrese sí o sí un valor numerico. Lo vi aqui: https://p-kane.medium.com/input-validation-with-python-570953d5d297
while True:
    try:
        edad = int(input("¿Cuántos años tienes?: "))
        if edad <= 0: 
            print(f"Por favor ingresa una edad válida")
        else:
            break    
    except ValueError:
        print(f"Por favor ingresa un número válido. No uses letras")

print(f"Excelente {nombre}, ahora necesito que por favor me brindes un par más de datos: ")

# Solicitar al usuario su peso y altura (definir variables de punto flotante)
while True:
        try:
            peso = float(input("Introduce tu peso en kilogramos: "))
            if peso <= 0:
                print(f"Por favor ingresa un peso válido")
            else:
                break
        except ValueError:
            print(f"Por favor no uses letras")

while True:
        try:
            altura = float(input("Introduce tu altura en metros: "))
            if altura <= 0:
                print(f"Por favor ingresa una altura válido")
            else:
                break
        except ValueError:
            print(f"Por favor no uses letras")

# Calcular el IMC del usuario
imc = float(peso/altura**2) 

# Imprimir el resultado del calculo del IMC
print(f"\n\n {nombre} {apellido_paterno} {apellido_materno} a tus {edad} años, tu IMC es: {imc : .2f} \n")

# Condicional para diferenciar en qué clasificación de IMC está el usuario
# Coloqué 6 decimales ya que de otro modo en algunas ocasiones de saltaba un error
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
