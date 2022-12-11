from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, items: dict[str, int], capacity: int):
        """
        Construct a new Storage object with the specified capacity \n
        :param items: Dictionary with the items to be stored
        :param capacity: The capacity of Storage object
        """
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, title: str, count: int) -> None:
        """
        Add an item in the storage \n
        :param title: Item title
        :param count: Item count
        :return: None
        """
        pass

    @abstractmethod
    def remove(self, title: str, count: int) -> None:
        """
        Remove an item from the storage \n
        :param title: Item title
        :param count: Item count
        :return: None
        """
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        """
        Get the free space in the storage \n
        :return: Free space
        """
        pass

    @abstractmethod
    def get_items(self) -> dict[str, int]:
        """
        Get the dict of items in the storage \n
        :return: Dictionary with items and count
        """
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        """
        Get the number of unique items in the storage \n
        :return: Number of unique items in the storage
        """
        pass
