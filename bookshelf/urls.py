from django.contrib import admin
from django.urls import path

from books.views import get_book_details_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<int:book_id>/', get_book_details_html),
]
