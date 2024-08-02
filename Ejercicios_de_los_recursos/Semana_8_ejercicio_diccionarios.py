emoji_diccionario = {"trufa": "🐕", "bb": "👶", "risa": "🤣", "sonrisa": "😊", "llorar": "😭", "beso": "😙", "aplauso": "👏", "reir" :"😆", "fuego": "🔥", "hola": "✋", "pensando": "🤔", "maravillado": "🤩", "aburrido": "🥱", "guiño": "😉", "ok": "👌", "abrazo": "🤗", "cool": "😎", "enojado": "😠", "python": "🐍"}

frase = input('Escribe una frase: ')
frase = frase.lower()
palabras = frase.split()
print(palabras)

respuesta = ''

for palabra in palabras:
    if palabra in emoji_diccionario:
        respuesta += emoji_diccionario[palabra] + ' '
    else:
        respuesta += palabra + ' '
print(respuesta)

