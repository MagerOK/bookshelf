from django.contrib import admin
from django.urls import path

from books.views import Get_All_Books_Json_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', Get_All_Books_Json_View.as_view()),
]
