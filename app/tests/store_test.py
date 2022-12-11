import pytest

from app.classes.store import Store
from app.exceptions import StoreNotEnoughSpaceError, IncorrectItemError, IncorrectItemCountError, CapacityLimitError


class TestStore:

    def test_create_store(self):
        with pytest.raises(CapacityLimitError):
            Store({"Яблоки": 101})

    def test_add(self):
        store = Store({"Яблоки": 10})

        with pytest.raises(StoreNotEnoughSpaceError):
            store.add("Яблоки", 91)
        with pytest.raises(StoreNotEnoughSpaceError):
            store.add("Коробки", 91)

    def test_remove(self):
        store = Store({"Яблоки": 10})

        with pytest.raises(IncorrectItemError):
            store.remove("Ананасы", 5)
        with pytest.raises(IncorrectItemCountError):
            store.remove("Яблоки", 11)

    def test_get_free_space(self):
        store = Store({"Яблоки": 10})

        assert type(store.get_free_space()) == int, "Возвращается не число"
        assert store.get_free_space() == 90, "Неверное количество свободного места"

    def test_get_items(self):
        store = Store({"Яблоки": 10})

        assert type(store.get_items()) == dict, "Не словарь"
        assert store.get_items() == {"Яблоки": 10}, "Не совпадают товары"

    def test_get_unique_items_count(self):
        store = Store({"Яблоки": 10})

        assert type(store.get_unique_items_count()) == int, "Возвращается не число"
        assert store.get_unique_items_count() == 1, "Количество уникальных товаров не совпадает"
