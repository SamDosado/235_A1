class Author:
    def __init__(self, author_id: int, author_name: str):
        if not isinstance(author_id, int) or author_id < 0 or not isinstance(author_name, str) or author_name.strip() == "":
            raise ValueError
        self.__author_id = author_id
        self.__author_name = author_name.strip()
        self.__coauthors = []

    @property
    def full_name(self):
        return self.__author_name

    @full_name.setter
    def full_name(self, author_name: str):
        if not isinstance(author_name, str) or author_name.strip() == "":
            raise ValueError
        self.__author_name = author_name.strip()

    @property
    def unique_id(self):
        return self.__author_id

    def __repr__(self):
        return f'<Author {self.__author_name}, author id = {self.__author_id}>'

    def __eq__(self, other):
        if not isinstance(other, Author):
            return False
        return self.__author_id == other.unique_id

    def __lt__ (self, other):
        if not isinstance(other, Author):
            return False
        return self.__author_id < other.unique_id

    def __hash__(self):
        return hash(self.__author_id)

    def add_coauthor(self, coauthor):
        if not isinstance(coauthor, Author):
            return False
        self.__coauthors.append(coauthor)

    def check_if_this_author_coauthored_with(self, author):
        return author in self.__coauthors
