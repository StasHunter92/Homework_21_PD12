import pytest

from app.classes.shop import Shop
from app.exceptions import IncorrectItemError, IncorrectItemCountError, CapacityLimitError, \
    UniqueItemsError, ShopNotEnoughSpaceError


class TestShop:

    def test_create_store(self):
        with pytest.raises(CapacityLimitError):
            Shop({"Яблоки": 21})

        with pytest.raises(UniqueItemsError):
            Shop({"Яблоки": 1, "Груши": 1, "Бананы": 1, "Апельсины": 1, "Ананасы": 1, "Сливы": 1})

    def test_add(self):
        shop = Shop({"Яблоки": 10})

        with pytest.raises(ShopNotEnoughSpaceError):
            shop.add("Яблоки", 11)
        with pytest.raises(ShopNotEnoughSpaceError):
            shop.add("Коробки", 11)
        with pytest.raises(UniqueItemsError):
            shop.add("Груши", 1)
            shop.add("Бананы", 1)
            shop.add("Апельсины", 1)
            shop.add("Ананасы", 1)
            shop.add("Сливы", 1)

    def test_remove(self):
        shop = Shop({"Яблоки": 10})

        with pytest.raises(IncorrectItemError):
            shop.remove("Ананасы", 5)
        with pytest.raises(IncorrectItemCountError):
            shop.remove("Яблоки", 11)

    def test_get_free_space(self):
        shop = Shop({"Яблоки": 10})

        assert type(shop.get_free_space()) == int, "Возвращается не число"
        assert shop.get_free_space() == 10, "Неверное количество свободного места"

    def test_get_items(self):
        shop = Shop({"Яблоки": 10})

        assert type(shop.get_items()) == dict, "Не словарь"
        assert shop.get_items() == {"Яблоки": 10}, "Не совпадают товары"

    def test_get_unique_items_count(self):
        shop = Shop({"Яблоки": 10})

        assert type(shop.get_unique_items_count()) == int, "Возвращается не число"
        assert shop.get_unique_items_count() == 1, "Количество уникальных товаров не совпадает"
