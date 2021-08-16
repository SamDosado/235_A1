class Publisher:

    def __init__(self, publisher_name):
        if (not isinstance(publisher_name, str)) or publisher_name.strip() == "":
            self.__name = "N/A"
        else:
            self.__name = publisher_name.strip()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, publisher_name):
        if isinstance(publisher_name, str) and publisher_name.strip() != "":
            self.__name = publisher_name.strip()

    def __repr__(self):
        # we use access via the property here
        return f'<Publisher {self.name}>'

    def __eq__(self, other):
        if not isinstance(other, Publisher):
            return False
        return other.name == self.__name

    def __lt__(self, other):
        if not isinstance(other, Publisher):
            return False
        return self.__name < other.name

    def __hash__(self):
        return hash(self.__name)

