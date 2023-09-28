from typing import TypedDict


class SerializedBook(TypedDict):
    title: str
    author_full_name: str
    year_of_publishing: int
    copies_printed: int
    short_description: str
