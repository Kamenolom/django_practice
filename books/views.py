from django.shortcuts import render
from .models import Book, Category
from django.db.models import Q, Count


def book_list(request):
    books = Book.objects.filter(stock__gt=0)
    categories = Category.objects.annotate(book_count=Count('book'))
    query = request.GET.get('q')
    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request,
                  'books/book_list.html',
                  {'books': books,
                   'categories': categories,
                   }
                  )
