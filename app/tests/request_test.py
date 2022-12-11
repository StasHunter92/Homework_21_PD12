import pytest

from app.classes.request import Request
from app.classes.shop import Shop
from app.classes.store import Store
from app.exceptions import IncorrectQueryError, RouteError


class TestRequest:

    def test_query_parse(self):
        with pytest.raises(IncorrectQueryError):
            Request("Доставить 3 печеньки из склад в магазин a",
                    {"склад": Store({"Печеньки": 10}), "магазин": Shop({"Печеньки": 10})})
        with pytest.raises(IncorrectQueryError):
            Request("Доставить T3 печеньки из склад в магазин",
                    {"склад": Store({"Печеньки": 10}), "магазин": Shop({"Печеньки": 10})})
        with pytest.raises(RouteError):
            Request("Доставить 3 печеньки из лавка в магазин",
                    {"склад": Store({"Печеньки": 10}), "магазин": Shop({"Печеньки": 10})})

    def test_get_amount(self):
        request = Request("Доставить 3 печеньки из склад в магазин",
                          {"склад": Store({"Печеньки": 10}), "магазин": Shop({"Печеньки": 10})})

        assert type(request.get_amount) == int, "Возвращается не число"
        assert request.get_amount == 3, "Неверное количество товара"

    def test_get_product(self):
        request = Request("Доставить 3 печеньки из склад в магазин",
                          {"склад": Store({"Печеньки": 10}), "магазин": Shop({"Печеньки": 10})})

        assert type(request.get_product) == str, "Возвращается не строка"
        assert request.get_product == "Печеньки", "Неверное наименование товара"

    def test_get_from(self):
        request = Request("Доставить 3 печеньки из склад в магазин",
                          {"склад": Store({"Печеньки": 10}), "магазин": Shop({"Печеньки": 10})})

        assert type(request.get_from) == Store, "Возвращается не тот экземпляр"

    def test_get_name_from(self):
        request = Request("Доставить 3 печеньки из склад в магазин",
                          {"склад": Store({"Печеньки": 10}), "магазин": Shop({"Печеньки": 10})})

        assert type(request.get_name_from) == str, "Возвращается не строка"
        assert request.get_name_from == "склад", "Возвращается неверное место"

    def test_get_to(self):
        request = Request("Доставить 3 печеньки из склад в магазин",
                          {"склад": Store({"Печеньки": 10}), "магазин": Shop({"Печеньки": 10})})

        assert type(request.get_to) == Shop, "Возвращается не тот экземпляр"

    def test_get_name_to(self):
        request = Request("Доставить 3 печеньки из склад в магазин",
                          {"склад": Store({"Печеньки": 10}), "магазин": Shop({"Печеньки": 10})})

        assert type(request.get_name_to) == str, "Возвращается не строка"
        assert request.get_name_to == "магазин", "Возвращается неверное место"
