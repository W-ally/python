'''This file have the purpose of ...'''

# Creando funciones.
# Llamando funciones.
# ¿Argumento o Parámetro?
# Un argumento.
# Varios argumentos.
# Argumentos arbitrarios. *args
# Argumentos llave-valor.
# Argumentos arbitrarios de llave-valor. **kwargs
# Parámetros por defecto.
# Lista como parámetro.
# returns.
# pass.

def favorite_food(*foods) -> str:
    return f'My favorite food is {foods[0]}'


def favorite_song(**songs) -> str:
    print(type(songs["data"]))
    return f'My favorite song is {songs["data"]["title"]}'

payload = {
    'title': 'Callaita',
    'song': 'The Sign',
    'artist': 'Ace of Base',
    'album': 'The Sign',
    'year': '2000',
    'genre': 'Rock'
}

print(favorite_song(data=payload))
print(favorite_food("Pizza", "Tacos", "Tacos"))