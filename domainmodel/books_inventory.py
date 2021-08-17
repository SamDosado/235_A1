from domainmodel.publisher import Publisher
from domainmodel.author import Author
from domainmodel.review import Review
from domainmodel.book import Book


class BooksInventory:

    def __init__(self,):
        self.__booksInventory = []

    @property
    def inventory(self):
        return self.__booksInventory

    def add_book(self, book, price, nr_books_in_stock):
        if not isinstance(book, Book) or (not isinstance(price, int) or not isinstance(price, float)) or not isinstance(nr_books_in_stock, int) or price < 0 or nr_books_in_stock < 0:
            self.__booksInventory.append({"book": book, "price": price, "stock": nr_books_in_stock})

    def remove_book(self, book_id):
        for book in self.__booksInventory:
            if book["book"].book_id == book_id:
                self.__booksInventory.remove(book)

    def find_price(self, book_id):
        for book in self.__booksInventory:
            if book["book"].book_id == book_id:
                return book["price"]

    def find_book(self, book_id):
        for book in self.__booksInventory:
            if book["book"].book_id == book_id:
                return book["book"]

    def find_stock_count(self, book_id):
        for book in self.__booksInventory:
            if book["book"].book_id == book_id:
                return book["stock"]

    def search_book_by_title(self, title):
        for book in self.__booksInventory:
            if book["book"].title == title:
                return book["book"]
