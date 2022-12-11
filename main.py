from app.classes.courier import Courier
from app.exceptions import IncorrectQueryError, IncorrectItemError, StoreNotEnoughSpaceError, ShopNotEnoughSpaceError, \
    IncorrectItemCountError, UniqueItemsError
from app.data.goods import goods_for_store, goods_for_shop
from app.classes.request import Request
from app.classes.shop import Shop
from app.classes.store import Store


# ----------------------------------------------------------------------------------------------------------------------
# Main function
def main():
    while True:

        user_input = input("\nВведите запрос в формате 'Доставить 3 яблоки из склад в магазин'\n"
                           "Для остановки программы введите 'стоп' или 'Стоп':\n")

        # Block for exit from program
        if user_input in ["стоп", "Стоп"]:
            exit()

        # Block for parsing user input
        try:
            req = Request(user_input, storages)
        except IncorrectQueryError as e:
            print(f"{e.message}")
            continue

        courier = Courier(req)

        # Block for moving an order
        try:
            courier.make_order()
        except IncorrectItemError as e:
            print(f"{e.message}")
        except IncorrectItemCountError as e:
            print(f"{e.message}")
        except (StoreNotEnoughSpaceError, ShopNotEnoughSpaceError, UniqueItemsError) as e:
            courier.return_order()
            print(f"{e.message}")

        print(f"\nНа складе хранится:")
        for k, v in store.get_items().items():
            print(f"{v} {k}")

        print(f"\nВ магазине хранится:")
        if len(shop.get_items()) > 0:
            for k, v in shop.get_items().items():
                print(f"{v} {k}")
        else:
            print("Товаров нет")


if __name__ == "__main__":
    # Construct storages
    store = Store(goods_for_store)
    shop = Shop(goods_for_shop)
    storages = {"склад": store, "магазин": shop}

    # Start program
    main()
