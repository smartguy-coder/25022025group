import pytest

from models import Person


@pytest.fixture()
def person() -> Person:
    oleg = Person('Oleg')
    return oleg


@pytest.fixture()
def another_person() -> Person:
    oleg = Person('Oleg')
    return oleg
