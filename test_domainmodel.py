import pytest

from domainmodel.publisher import Publisher

class TestPublisher:

    def test_construction_valid(self):
        publisher1 = Publisher(" Bloomsbury")
        assert str(publisher1) == "<Publisher Bloomsbury>"
        publisher3 = Publisher("  DC Comics ")
        assert str(publisher3) == "<Publisher DC Comics>"


    def test_construction_invalid(self):
        publisher2 = Publisher("  ")
        assert str(publisher2) == "<Publisher N/A>"
        publisher4 = Publisher(42)
        assert str(publisher4) == "<Publisher N/A>"
