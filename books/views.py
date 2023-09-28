from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from books.models import Book
from books.serializer import serialize_book


class Get_All_Books_Json_View(View):
    def get(self, request: HttpResponse) -> JsonResponse:
        books = Book.objects.all()
        books_json = [serialize_book(book) for book in books]
        return JsonResponse(data={'data': books_json})
