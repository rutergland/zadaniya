import requests

response = requests.get(
    "https://pokeapi.co/api/v2/pokemon?limit=20",
    timeout=10,
)
response.raise_for_status()
data = response.json()
print("Список покемонов:")
for pokemon in data["results"]:
    print(pokemon["name"])
name = input("Имя покемона:").strip().lower()

response = requests.get(
    f"https://pokeapi.co/api/v2/pokemon/{name}",
    timeout=10,
)
response.raise_for_status()

pokemon = response.json()

print("Имя:", pokemon["name"])
types = []
for item in pokemon["types"]:
    types.append(item["type"]["name"])
print("Тип:", ", ".join(types))
print("Вес:", pokemon["weight"])
print("Рост:", pokemon["height"])
abilities = []
for item in pokemon["abilities"]:
    abilities.append(item["ability"]["name"])
print("Способности:", ", ".join(abilities))
