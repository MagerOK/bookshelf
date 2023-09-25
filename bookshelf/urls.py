from django.contrib import admin
from django.urls import path

from books.views import get_book_json_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/<int:book_id>/', get_book_json_view)
]
