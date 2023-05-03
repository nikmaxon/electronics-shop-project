import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    file_name = 'items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return int(self.quantity + other.quantity)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            print('Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open(f'../src/{cls.file_name}', encoding='windows-1251') as f:
                reader = csv.DictReader(f)
                if len(list(csv.reader(f))[0]) != 3:
                    raise InstantiateCSVError(f'Файл {cls.file_name} поврежден')
                f.seek(0)
                for word in reader:
                    cls.all.append(cls(word['name'], word['price'], word['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {cls.file_name}')
        except PermissionError:
            print(f'Невозможно создать файл {cls.file_name}')

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.quantity * self.price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate


class InstantiateCSVError(Exception):
    pass
