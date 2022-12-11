from app.classes.abstract_storage import Storage
from app.exceptions import IncorrectQueryError, RouteError


# ----------------------------------------------------------------------------------------------------------------------
# Request class for parsing user input
class Request:
    def __init__(self, query: str, route: dict[str, Storage]):
        if len(query.split()) != 7 or not query.split()[1].isdigit():
            raise IncorrectQueryError

        self.__amount = int(query.split()[1])
        self.__product = query.split()[2].capitalize()
        self.__from = query.split()[4].lower()
        self.__to = query.split()[6].lower()

        self.__route = route

        if self.__from not in route or self.__to not in route:
            raise RouteError

    @property
    def get_amount(self) -> int:
        """
        Get the amount of the requested item \n
        :return: Amount of the requested item
        """
        return self.__amount

    @property
    def get_product(self) -> str:
        """
        Get the name of requested item \n
        :return: Name of the requested item
        """
        return self.__product

    @property
    def get_from(self) -> Storage:
        """
        Get the instance of the requested departure point \n
        :return: Instance of the requested departure point
        """
        return self.__route[self.__from]

    @property
    def get_name_from(self) -> str:
        """
        Get the name of the requested departure point \n
        :return: Name of the requested departure point
        """
        return self.__from

    @property
    def get_to(self) -> Storage:
        """
        Get the instance of the requested destination point \n
        :return: Instance of the requested destination point
        """
        return self.__route[self.__to]

    @property
    def get_name_to(self) -> str:
        """
        Get the name of the requested destination point \n
        :return: Name of the requested destination point
        """
        return self.__to
