import time

from app.classes.request import Request


# ----------------------------------------------------------------------------------------------------------------------
# Courier class to move goods between storages
class Courier:
    def __init__(self, request: Request):
        self.__request = request

    def make_order(self) -> None:
        """
        Takes a request and move goods between storages \n
        :return: None
        """
        self.__request.get_from.remove(self.__request.get_product, self.__request.get_amount)
        print(f"\nКурьер забрал {self.__request.get_amount} {self.__request.get_product} "
              f"из {self.__request.get_name_from}")
        time.sleep(1)

        print(f"Курьер везет {self.__request.get_amount} {self.__request.get_product} "
              f"из {self.__request.get_name_from} в {self.__request.get_name_to} ")
        time.sleep(1)

        self.__request.get_to.add(self.__request.get_product, self.__request.get_amount)
        print(f"Курьер доставил {self.__request.get_amount} {self.__request.get_product} "
              f"в {self.__request.get_name_to} ")

    def return_order(self) -> None:
        """
        Returns the order if destination is unavailable \n
        :return: None
        """
        self.__request.get_from.add(self.__request.get_product, self.__request.get_amount)
