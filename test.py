
import requests

response = requests.get("https://img.pokemondb.net/artwork/pikachu.jpg")


f_name = 'pikachi.png'
file = open('img/' + f_name, "wb")

file.write(response.content)

file.close()