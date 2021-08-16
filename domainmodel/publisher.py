class Publisher:

    def __init__(self, publisher_name):
        if (not isinstance(publisher_name, str)) or publisher_name.strip() == "":
            self.__name = "N/A"
        else:
            self.__name = publisher_name.strip()

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, publisher_name):
        if isinstance(publisher_name, str) and publisher_name.strip() != "":
            self.__name = publisher_name.strip()

    def __repr__(self):
        # we use access via the property here
        return f'<Publisher {self.name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.name == self.name

    def __lt__(self, other):
        if self.__name < other.name:
            return True
        return False


    def __hash__(self):
        return hash(self.__name)

