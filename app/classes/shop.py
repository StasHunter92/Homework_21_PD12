from app.classes.abstract_storage import Storage
from app.exceptions import UniqueItemsError, CapacityLimitError, ShopNotEnoughSpaceError, IncorrectItemError, \
    IncorrectItemCountError, FreeSpaceError


# ----------------------------------------------------------------------------------------------------------------------
# Shop class inherited from abstract storage
class Shop(Storage):
    def __init__(self, items: dict, capacity=20):
        if len(items) > 5:
            raise UniqueItemsError

        if capacity >= sum(title for title in items.values()):
            super().__init__(items, capacity)
        else:
            raise CapacityLimitError

    def add(self, title: str, count: int) -> None:
        """
        Add an item in the storage \n
        :param title: Item title
        :param count: Item count
        :return: None
        """
        if title not in self.get_items():
            if self.get_unique_items_count() >= 5:
                raise UniqueItemsError

            if count <= self.get_free_space():
                self.get_items()[title] = count
            else:
                raise ShopNotEnoughSpaceError
        else:
            if count <= self.get_free_space():
                self.get_items()[title] += count
            else:
                raise ShopNotEnoughSpaceError

    def remove(self, title: str, count: int) -> None:
        """
        Remove an item from the storage \n
        :param title: Item title
        :param count: Item count
        :return: None
        """
        if title not in self.get_items():
            raise IncorrectItemError

        if count > self.get_items()[title]:
            raise IncorrectItemCountError

        self.get_items()[title] -= count

        if self.get_items()[title] == 0:
            self.get_items().pop(title)

    def get_free_space(self) -> int:
        """
        Get the free space in the storage \n
        :return: Free space
        """
        free_space = self._capacity - sum(self.get_items().values())

        if free_space < 0:
            raise FreeSpaceError

        return free_space

    def get_items(self) -> dict:
        """
        Get the dict of items in the storage \n
        :return: Dictionary with items and count
        """
        return self._items

    def get_unique_items_count(self) -> int:
        """
        Get the number of unique items in the storage \n
        :return: Number of unique items in the storage
        """
        return len(self.get_items())
