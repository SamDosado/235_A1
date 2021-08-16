import pytest

from domainmodel.publisher import Publisher
from domainmodel.author import Author
from domainmodel.book import Book


class TestPublisher:

    def test_publisher_construction_valid(self):
        publisher1 = Publisher(" Bloomsbury")
        assert str(publisher1) == "<Publisher Bloomsbury>"
        publisher3 = Publisher("  DC Comics ")
        assert str(publisher3) == "<Publisher DC Comics>"


    def test_publisher_construction_invalid(self):
        publisher2 = Publisher("  ")
        assert str(publisher2) == "<Publisher N/A>"
        publisher4 = Publisher(42)
        assert str(publisher4) == "<Publisher N/A>"

    def test_publisher_setter_valid(self):
        publisher5 = Publisher("  ")
        publisher5.name = "Bloomsbury"
        assert str(publisher5) == "<Publisher Bloomsbury>"
        publisher6 = Publisher(42)
        publisher6.name = "DC Comics"
        assert str(publisher6) == "<Publisher DC Comics>"

    def test_publisher_setter_invalid(self):
        publisher7 = Publisher("Bloomsbury")
        publisher7.name = "  "
        assert str(publisher7) == "<Publisher Bloomsbury>"
        publisher8 = Publisher("DC Comics")
        publisher8.name = 42
        assert str(publisher8) == "<Publisher DC Comics>"

    def test_author_constructor_valid(self):
        author = Author(0, "Samuel Dosado")
        assert str(author) == "<Author Samuel Dosado, author id = 0>"
        author1 = Author(1, "John Smith")
        assert str(author1) == "<Author John Smith, author id = 1>"

    def test_author_constructor_invalid(self):
        try:
            author2 = Author(-1, "Samuel Dosado ")
        except ValueError:
            assert True
        try:
            author3 = Author(3, " John Smith")
        except ValueError:
            assert True


    def test_author_setter_valid(self):
        author4 = Author(4, "Samuel Dosado")
        author4.full_name = "John Smith"
        assert str(author4) == "<Author John Smith, author id = 4>"
        author5 = Author(5, "John Smith")
        author5.full_name = "Samuel Dosado"
        assert str(author5) == "<Author Samuel Dosado, author id = 5>"


    def test_author_setter_invalid(self):
        try:
            author6 = Author(6, "Samuel Dosado ")
            author6.unique_id = 1
        except AttributeError:
            assert True
        author7 = Author(7, "John Smith ")
        try:
            author7.full_name = " "
        except ValueError:
            assert True
        assert str(author7) == "<Author John Smith, author id = 7>"

    def test_book_contructor_valid(self):
        book = Book(0, "A Book ")
        assert str(book) == "<Book A Book, book id = 0>"
        book1 = Book(1, " Lord Of The Rings")
        assert str(book1) == "<Book Lord Of The Rings, book id = 1>"

    def test_book_constructor_invalid(self):
        try:
            book2 = Book(-1, "A Book")
        except ValueError:
            assert True
        try:
            book3 = Book(3, " ")
        except ValueError:
            assert True

    def test_book_setter_valid(self):
        book4 = Book(4, "A Wonderful Day")
        publisher = Publisher("Bloomsbury")
        book4.publisher = publisher
        assert book4.publisher == publisher
        book5 = Book(5, "Harry Potter")
        book5.release_year = 1991
        assert book5.release_year == 1991
        book6 = Book(6, "The Lion The Witch and The Wardrobe")
        book6.description = "What a good read!"
        assert book6.description == "What a good read!"
        book7 = Book(7, "Sorry Wrong Name")
        book7.title = "This is the right name "
        assert book7.title == "This is the right name"
        authors = [Author(0, "Samuel Dosado"), Author(1, "John Smith")]
        book8 = Book(8, "How to write test cases")
        book8.authors = authors
        assert book8.authors == authors


    def test_book_setter_invalid(self):
        book9 = Book(9, "A Wonderful Day")
        book9.publisher = "Bloomsbury"
        assert book9.publisher == None
        book10 = Book(10, "Harry Potter")
        try:
            book10.release_year = " "
        except ValueError:
            assert True
        assert book10.release_year == None
        book11 = Book(11, "The Lion The Witch and The Wardrobe")
        book11.description = 12
        assert book11.description == None
        book12 = Book(12, "Sorry Wrong Name")
        try:
            book12.title = 15
        except ValueError:
            assert True
        assert book12.title == "Sorry Wrong Name"
        book13 = Book(13, "How to write test cases")
        book13.authors = "Samuel Dosado"
        assert book13.authors == []

