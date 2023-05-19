# Вызываем импорты
import csv
import os

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
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.__name

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
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        with open(path_to_file, encoding="windows-1251") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')

            for row in reader:
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
