from domainmodel.publisher import Publisher
from domainmodel.author import Author
from domainmodel.book import Book
import datetime


class Review:

    def __init__(self, book, review_text, rating):
        if isinstance(book, Book):
            self.__book = book
        else:
            raise ValueError
        if isinstance(review_text, str) and review_text.strip() != "":
            self.__review_text = review_text.strip()
        else:
            self.__review_text = "N/A"
        if isinstance(rating, int) and 1 <= rating <= 5:
            self.__rating = rating
        else:
            raise ValueError
        self.__timestamp = datetime.datetime.now()

    @property
    def book(self):
        return self.__book

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return f"{self.__book}, review {self.__review_text}, rating: {self.__rating}"

    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        return str(self) == str(other)
