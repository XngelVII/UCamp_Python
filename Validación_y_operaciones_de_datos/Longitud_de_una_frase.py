palabra = input("Por favor introduce una palabra:")
letras = len(palabra)
if 3 < len(palabra) < 9:
    print(f"\nLa longitud de la palabra es correcta.")
elif len(palabra) < 4:
    faltan = 4 - letras 
    if faltan == 1:
        print(f"\nLa palabra {palabra} solo tiene {letras} letras. \nFalta {faltan} letra")
    else:
        print(f"\nLa palabra {palabra} solo tiene {letras} letras. \nFaltan {faltan} letras")
elif len(palabra) > 8:
    sobran = letras - 8
    if sobran == 1:
        print(f"\nLa palabra {palabra} tiene {letras} letras. \nSobra {sobran} letra")
    else:
        print(f"\nLa palabra {palabra} tiene {letras} letras. \nSobran {sobran} letras")
