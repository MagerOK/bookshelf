from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404, HttpResponse

from books.models import Book
from books.serializer import serialize_book


def get_book_json_view(request: HttpResponse, book_id: int) -> HttpResponse:
    book = Book.objects.filter(pk=book_id).first()
    if not book:
        return JsonResponse(data={'data': {}, "error": "Book not found"}, status=404)
    serialized_book = serialize_book(book)
    return JsonResponse(data={'data': serialized_book})

def get_book_details_html(request: HttpResponse, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'book_details.html', context)

def get_all_books_html_view(request: HttpResponse) -> HttpResponse:
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books_table.html', context)
