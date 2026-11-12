import requests

team = {}


def add(name):
    if name in team:
        print("Покемон уже в команде")
        return

    pokemon = find(name)
    if pokemon is not None:
        team[name] = pokemon
        print("Покемон добавлен")


def delete(name):
    if name not in team:
        print("Такого покемона нету в команде")
    else:
        del team[name]
        print("Покемон удалён")


def show(name):
    pokemon = team[name]
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


def find(name):
    try:
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{name}", timeout=10
        )
        if response.status_code == 404:
            print("Покемон не найден")
            return None
        response.raise_for_status()
        return response.json()

    except requests.RequestException:
        print("Не удалось получить данные")
        return None


def battle(f_pokemon, s_pokemon):
    if f_pokemon not in team or s_pokemon not in team:
        print("Оба покемона должны быть в команде")
        return

    if f_pokemon == s_pokemon:
        print("Выбери двух разных покемонов")
        return

    first_score = 0
    for item in team[f_pokemon]["stats"]:
        first_score += item["base_stat"]

    second_score = 0
    for item in team[s_pokemon]["stats"]:
        second_score += item["base_stat"]

    print(f"{f_pokemon}: {first_score} очков")
    print(f"{s_pokemon}: {second_score} очков")

    if first_score > second_score:
        print("Победил", f_pokemon)
    elif second_score > first_score:
        print("Победил", s_pokemon)
    else:
        print("Ничья")


while True:
    choose = int(input(
        "Выберите действие 1-add, 2-delete, 3-find, 4-show, 5-battle: "
        ))
    if choose == 1:
        name = input("Введите имя покемона: ").strip().lower()
        add(name)
    if choose == 2:
        name = input("Введите имя покемона: ").strip().lower()
        delete(name)
    if choose == 3:
        name = input("Введите имя покемона: ").strip().lower()
        print(find(name))
    if choose == 4:
        for name in team:
            show(name)
    if choose == 5:
        f_pokemon = input("Выберите покемона по имени: ").strip().lower()
        s_pokemon = input("Выберите покемона по имени: ").strip().lower()
        battle(f_pokemon, s_pokemon)
