from django.shortcuts import render


def book_detail(request):
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
