import time

from app.classes.request import Request


# ----------------------------------------------------------------------------------------------------------------------
# Courier class to move goods between storages
class Courier:
    def __init__(self, request: Request):
        self.request = request

    def make_order(self) -> None:
        """
        Takes a request and move goods between storages \n
        :return: None
        """
        self.request.get_from().remove(self.request.get_product(), self.request.get_amount())
        print(f"\nКурьер забрал {self.request.get_amount()} {self.request.get_product()} "
              f"из {self.request.get_name_from()}")
        time.sleep(1)

        print(f"Курьер везет {self.request.get_amount()} {self.request.get_product()} "
              f"из {self.request.get_name_from()} в {self.request.get_name_to()} ")
        time.sleep(1)

        self.request.get_to().add(self.request.get_product(), self.request.get_amount())
        print(f"Курьер доставил {self.request.get_amount()} {self.request.get_product()} "
              f"в {self.request.get_name_to()} ")

    def return_order(self) -> None:
        """
        Returns the order if destination is unavailable
        :return: None
        """
        self.request.get_from().add(self.request.get_product(), self.request.get_amount())
