from django.shortcuts import render


def book_detail(request):
    books = [
        {
            'title': 'Big Black Book',
            'author': 'Big Black Author',
            'year': '2000',
            'price': 1250.5,
        },
        {
            'title': 'Small Black Book',
            'author': 'Small Black Author',
            'year': '2',
            'price': 89.99,
        }
    ]
    return render(request, 'catalog/book_detail.html', {'books': books})
