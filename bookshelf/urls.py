from django.contrib import admin
from django.urls import path
from django.urls import include

from books.views import get_book_json_view, get_book_details_html, get_all_books_html_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', get_all_books_html_view),
    path('book/<int:book_id>/', get_book_details_html),
    path('api/books/<int:book_id>/', get_book_json_view),
]
