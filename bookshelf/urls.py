from django.contrib import admin
from django.urls import path

from books.views import get_book_json_view, get_book_details_html


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<int:book_id>/', get_book_details_html),
    path('api/books/<int:book_id>/', get_book_json_view),
]
