from django.shortcuts import render
from django.http import JsonResponse

from books.models import Book
from books.serializer import serialize_book




def get_book_json_view(request, book_id: int):
    book = Book.objects.filter(pk=book_id).first()
    if not book:
        return JsonResponse(data={'data': {}, "error": "Book not found"}, status=404)
    serialized_book = serialize_book(book)
    return JsonResponse(data={'data': serialized_book})