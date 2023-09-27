from typing import TypedDict

from books.models import Book


class SerializedBook(TypedDict):
    title: str
    author_full_name: str
    year_of_publishing: int
    copies_printed: int
    short_description: str

def serialize_book(book: Book) -> SerializedBook:
    return {
        "title": book.title,
        "author_full_name": book.author_full_name,
        "year_of_publishing": book.year_of_publishing,
        "copies_printed": book.copies_printed,
        "short_description": book.short_description,
    }
