import requests

team = {}


def add(name):
    """Добавляет покемона в командный словарь team.
    Если покемон уже есть в команде, выводит сообщение об этом.
    В противном случае ищет покемона через find() и,
    если находит, сохраняет его в team.
    Args:
        name (str): Имя покемона для добавления.
    Returns:
        None
    """
    if name in team:
        print("Покемон уже в команде")
        return

    pokemon = find(name)
    if pokemon is not None:
        team[name] = pokemon
        print("Покемон добавлен")


def delete(name):
    """Удаляет покемона из командного словаря team.
    Если покемона нет в команде, выводит соответствующее сообщение.
    В противном случае удаляет запись из team.
    Args:
        name (str): Имя покемона для удаления.
    Returns:
        None
    """
    if name not in team:
        print("Такого покемона нету в команде")
    else:
        del team[name]
        print("Покемон удалён")


def show(name):
    """Выводит подробную информацию о покемоне из команды.
    Отображает имя, тип, вес, рост и способности покемона.
    Предполагается, что покемон уже есть в team.
    Args:
        name (str): Имя покемона из team, информацию о котором нужно показать.
    Returns:
        None
    """
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
    """Ищет покемона по имени через PokeAPI.
    Выполняет GET-запрос к PokeAPI. Если покемон не найден (404),
    выводит сообщение и возвращает None. При других ошибках запроса
    также выводит сообщение и возвращает None.
    Args:
        name (str): Имя покемона для поиска.
    Returns:
        dict | None: Словарь с данными покемона при успехе, иначе None.
    """
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
    """Проводит битву между двумя покемонами из команды.
    Сравнивает суммы базовых характеристик (base_stat) обоих покемонов.
    Выводит счёт и объявляет победителя или ничью.
    Если хотя бы одного покемона нет в team или имена совпадают,
    выводит сообщение об ошибке и завершает работу.
    Args:
        f_pokemon (str): Имя первого покемона.
        s_pokemon (str): Имя второго покемона.
    Returns:
        None
    """
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
