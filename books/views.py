from django.shortcuts import render, get_object_or_404

from books.models import Book

def get_book_details_html(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'book_details.html', context)