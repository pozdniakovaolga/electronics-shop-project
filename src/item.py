# Вызываем импорты
import csv
import os
from src.icsverror_class import InstantiateCSVError


# Определяем путь к файлу данных в переменную
path_to_src = os.path.abspath("../src/")
path_to_file = os.path.join(path_to_src, "items.csv")


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self) -> str:
        """
        Возвращает информацию об объекте: название класса(атрибуты экземпляра)
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """
        Возвращает информацию об объекте: название товара
        """
        return self.__name

    def __add__(self, other):
        """
        Реализует возможность сложения экземпляров класса по количеству товара в магазине
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError('Недопустимо сложение экземпляров классов Phone или Item с экземплярами не Phone или Item')

    @property
    def name(self) -> str:
        """
        Возвращает название товара
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Присваивает атрибуту name значение new_name,
        при условии, что длина названия товара не больше 10 символов
        """
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception(f'Длина наименования товара "{new_name}" превышает 10 символов')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return None

    @classmethod
    def instantiate_from_csv(cls, path=path_to_file) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        if not os.path.isfile(path):
            raise FileNotFoundError("Отсутствует файл items.csv")
        else:
            with open(path, encoding="windows-1251") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    if row['price'] is None or row['price'] == '':
                        raise InstantiateCSVError("Файл items.csv поврежден")
                    elif row['quantity'] is None or row['quantity'] == '':
                        raise InstantiateCSVError("Файл items.csv поврежден")
                    else:
                        name = str(row['name'])
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                        cls(name, price, quantity)

    @staticmethod
    def string_to_number(str_number: str) -> int:
        """
        Возвращает число из числа-строки
        """
        return int(float(str_number))
