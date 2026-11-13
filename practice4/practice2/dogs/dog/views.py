from django.shortcuts import render
import requests


def index(request):
    """Отображает страницу с фотографиями собак выбранных пород.
    Получает список всех пород с Dog API. Из GET-параметра "breeds"
    считывает породы, введённые пользователем (через запятую), проверяет
    их наличие и для каждой существующей породы запрашивает случайное фото.
    Результаты передаются в шаблон dog/index.html.
    Args:
        request (HttpRequest): Объект HTTP-запроса от Django.
    Returns:
        HttpResponse: Отрендеренная HTML-страница с фотографиями собак.
    """
    response = requests.get(
        "https://dog.ceo/api/breeds/list/all",
        timeout=10,
    )
    response.raise_for_status()
    dogs = response.json()["message"].keys()
    entered = request.GET.get("breeds", "")
    chosen = []
    for name in entered.split(","):
        if name.strip():
            chosen.append(name.strip().lower())
    photos = []
    for name in chosen:
        if name in dogs:
            photo_response = requests.get(
                f"https://dog.ceo/api/breed/{name}/images/random",
                timeout=10,
            )
            photo_response.raise_for_status()
            photos.append({
                "breed": name,
                "url": photo_response.json()["message"],
            })
    return render(
        request,
        "dog/index.html",
        {
            "all_breeds": sorted(dogs),
            "entered": entered,
            "photos": photos,
        },
    )
