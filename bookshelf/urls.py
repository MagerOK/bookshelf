from django.contrib import admin
from django.urls import path

from books.views import get_all_books_json_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', get_all_books_json_view),
]
