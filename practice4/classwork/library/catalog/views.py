from django.shortcuts import render


def book_detail(request):
    """Отображает страницу со списком книг.
    Формирует статический список книг (словарей с полями title, author, year)
    и передаёт его в шаблон catalog/book_detail.html.
    Args:
        request (HttpRequest): Объект HTTP-запроса от Django.
    Returns:
        HttpResponse: Отрендеренная HTML-страница со списком книг.
    """
    books = [
        {
            'title': 'Big Black Book',
            'author': 'Big Black Author',
            'year': '2000',
        },
        {
            'title': 'Small Black Book',
            'author': 'Small Black Author',
            'year': '2',
        }
    ]
    return render(request, 'catalog/book_detail.html', {'books': books})
