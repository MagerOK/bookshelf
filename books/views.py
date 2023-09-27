from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from books.models import Book
from books.serializer import serialize_book


def get_all_books_json_view(request: HttpResponse) -> HttpResponse:
    books = Book.objects.all()
    if not books:
        return JsonResponse(data={'data': {}, 'error': 'No books found'})
    books_json = [serialize_book(book) for book in books]
    return JsonResponse(data={'data': books_json})
