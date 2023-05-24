import pytest
from src.item import Item


@pytest.fixture
def item_fixture():
    return Item("Смартфон", 10000, 20)


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test___repr__(item_fixture):
    assert repr(item_fixture) == "Item('Смартфон', 10000, 20)"


def test___str__(item_fixture):
    assert str(item_fixture) == 'Смартфон'


def test___add__(item_fixture):
    assert item_fixture + item_fixture == 40


def test___add__typeerror(item_fixture):
    with pytest.raises(TypeError):
        item_fixture + 10


def test_adding_name(item_fixture):
    item_fixture.name = "Телефон"
    assert item_fixture.name == "Телефон"


def test__adding_name_exception(item_fixture):
    with pytest.raises(Exception):
        item_fixture.name = "СуперСмартфон"


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
