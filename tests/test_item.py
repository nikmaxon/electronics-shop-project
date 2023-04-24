import pytest
from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str(item):
    assert str(item) == 'Смартфон'


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0


def test_name_setter(item):
    item.name = 'Телефон'
    assert item.name == 'Телефон'
    item.name = 'СуперСмартфон'
    assert item.name == 'Телефон'


def test_instantiate_from_csv(item):
    item.instantiate_from_csv()
    assert len(item.all) == 5
    assert item.all[0].name == 'Смартфон'


def test_string_to_number(item):
    assert isinstance(item.string_to_number(item.quantity), int)
