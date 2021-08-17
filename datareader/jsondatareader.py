import json
from domainmodel.publisher import Publisher
from domainmodel.author import Author
from domainmodel.book import Book


class BooksJSONReader:

    def __init__(self, books_file_name: str, authors_file_name: str):
        if not isinstance(books_file_name, str) or not isinstance(authors_file_name, str):
            if books_file_name.strip() == "" or authors_file_name.strip() == "":
                raise ValueError
        self.__books_file_name = books_file_name.strip()
        self.__authors_file_name = authors_file_name.strip()
        self.__dataset_of_books = []

    @property
    def dataset_of_books(self) -> list:
        return self.__dataset_of_books

    def read_json_files(self):
        authors = []
        try:
            with open(self.__authors_file_name) as authors_file:
                for author in authors_file.readlines():
                    json_line = json.loads(author)
                    author = Author(int(json_line["author_id"]), json_line["name"])
                    authors.append(author)

            with open(self.__books_file_name) as books_file:
                for book in books_file.readlines():
                    json_line = json.loads(book)
                    book = Book(int(json_line["book_id"]), json_line["title"])
                    for book_author in json_line["authors"]:
                        for author in authors:
                            if author.unique_id == int(book_author["author_id"]):
                                book.add_author(author)
                    try:
                        book.release_year = int(json_line["publication_year"])
                    except ValueError:
                        pass
                    book.description = json_line["description"]
                    book.publisher = Publisher(json_line["publisher"])
                    self.__dataset_of_books.append(book)
        except FileNotFoundError:
            raise ValueError
