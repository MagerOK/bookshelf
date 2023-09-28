from books.models import Book
from books.types import SerializedBook


def serialize_book(book: Book) -> SerializedBook:
    return {
        "title": book.title,
        "author_full_name": book.author_full_name,
        "year_of_publishing": book.year_of_publishing,
        "copies_printed": book.copies_printed,
        "short_description": book.short_description,
    }
