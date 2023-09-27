from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from books.models import Book

def get_book_details_html(request: HttpResponse, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'book_details.html', context)