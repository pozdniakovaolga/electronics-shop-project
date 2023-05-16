import pytest
from src.item import Item


@pytest.fixture
def item_fixture():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item_fixture_2():
    return Item("Телефон", 10000, 5)


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_adding_name(item_fixture_2):
    item_fixture_2.name = "Смартфон"
    assert item_fixture_2.name == "Смартфон"


def test_adding_name_2(item_fixture_2):
    item_fixture_2.name = "СуперСмартфон"
    assert item_fixture_2.name == "Телефон"


def test_calculate_total_price(item_fixture):
    assert item_fixture.calculate_total_price() == 200000


def test_apply_discount(item_fixture):
    Item.pay_rate = 0.8
    item_fixture.apply_discount()
    assert item_fixture.price == 8000.0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
