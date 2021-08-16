from domainmodel.publisher import Publisher
from domainmodel.author import Author


class Book:

    def __init__(self, book_id: int, book_title: str):
        if not isinstance(book_id, int) or book_id < 0 or not isinstance(book_title, str) or book_title.strip() == "":
            raise ValueError
        self.__book_title = book_title.strip()
        self.__book_id = book_id
        self.__description = None
        self.__publisher = None
        self.__authors = []
        self.__release_year = None
        self.__ebook = None

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__book_title

    @title.setter
    def title(self, book_title):
        if not isinstance(book_title, str) or book_title.strip() == "":
            raise ValueError
        self.__book_title = book_title.strip()

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if isinstance(description, str) and description.strip() != "":
            self.__description = description.strip()

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors):
        if isinstance(authors, list):
            self.__authors = authors

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, release_year):
        if not isinstance(release_year, int) or release_year < 0:
            raise ValueError
        self.__release_year = release_year

    @property
    def ebook(self):
        return self.__ebook

    @ebook.setter
    def ebook(self, ebook):
        if isinstance(ebook, bool):
            self.__ebook = ebook

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher):
        if isinstance(publisher, Publisher):
            self.__publisher = publisher

    def add_author(self, author):
        if isinstance(author, Author):
            for a in self.__authors:
                if isinstance(a, Author):
                    a.add_coauthor(author)
            self.__authors.append(author)

    def remove_author(self, author):
        if isinstance(author, Author) and author in self.__authors:
            self.__authors.remove(author)

    def __repr__(self):
        return f'<Book {self.__book_title}, book id = {self.__book_id}>'

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.__book_id == other.book_id

    def __lt__(self, other):
        if not isinstance(other, Book):
            return False
        return self.__book_id < other.book_id

    def __hash__(self):
        return hash(self.__book_id)
