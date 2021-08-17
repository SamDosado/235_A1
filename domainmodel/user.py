from domainmodel.publisher import Publisher
from domainmodel.author import Author
from domainmodel.review import Review
from domainmodel.book import Book


class User:
    def __init__(self, user_name, password):
        if isinstance(user_name, str) and user_name.strip() != "":
            self.__user_name = user_name.strip().lower()
        else:
            self.__user_name = None
        if isinstance(password, str) and len(password.strip()) >= 7:
            self.__password = password.strip()
        else:
            self.__password = None
        self.__read_books = []
        self.__reviews = []
        self.__pages_read = 0

    @property
    def read_books(self):
        return self.__read_books

    @property
    def pages_read(self):
        return self.__pages_read

    @property
    def reviews(self):
        return self.__reviews

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    def __repr__(self):
        return f'<User {self.__user_name}>'

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.__user_name == other.user_name

    def __lt__(self, other):
        if not isinstance(other, User):
            return False
        return self.__user_name < other.user_name

    def __hash__(self):
        return hash(self.__user_name)

    def read_a_book(self, book):
        if isinstance(book, Book):
            self.__pages_read += book.num_pages
            self.__read_books.append(book)

    def add_review(self, review):
        if isinstance(review, Review):
            self.__reviews.append(review)