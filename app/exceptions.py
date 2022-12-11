class BaseError(Exception):
    message = "Неизвестная ошибка"


class CapacityLimitError(BaseError):
    message = "Вы пытаетесь разместить больше товаров чем возможно"


class StoreNotEnoughSpaceError(BaseError):
    message = "Недостаточно места на складе"


class ShopNotEnoughSpaceError(BaseError):
    message = "Недостаточно места в магазине"


class IncorrectItemError(BaseError):
    message = "Нет такого товара"


class IncorrectItemCountError(BaseError):
    message = "У товара не хватит запрашиваемого количества"


class FreeSpaceError(BaseError):
    message = "Недостаточно свободного места"


class UniqueItemsError(BaseError):
    message = "Уникальных товаров не может быть больше 5"


class IncorrectQueryError(BaseError):
    message = "Некорректный запрос"


class RouteError(BaseError):
    message = "Такого пункта нет"
