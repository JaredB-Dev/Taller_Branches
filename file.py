# Lista de las 10 mejores canciones
canciones = [
    "Bohemian Rhapsody - Queen",
    "Imagine - John Lennon",
    "Stairway to Heaven - Led Zeppelin",
    "Say My Name - Bettle Juice",
    "Queen - Bohemian Rhapsody",
    "John Lennon - Imagine",
    "Led Zeppelin - Stairway to Heaven",
    "Hey Jude - The Beatles",
    "Smells Like Teen Spirit - Nirvana",
    "Hotel California - Eagles",
    "Like a Rolling Stone - Bob Dylan",
    "Billie Jean - Michael Jackson",
    "Sweet Child O' Mine - Guns N' Roses",
    "Wonderwall - Oasis"
]
info = "Esta es una lista de las 10 mejores canciones de todos los tiempos. Las canciones están ordenadas alfabéticamente y se les asigna un número de índice."
# Ordenar la lista en orden ascendente (alfabético)
canciones_ordenadas = sorted(canciones)[::-1]

# Imprimir la lista ordenada
i = 1
for cancion in canciones_ordenadas:
    print(f"{cancion} + {i} *_*")
    i += 1

print(info)