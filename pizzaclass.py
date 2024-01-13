from typing import Type


class PizzaClass:
    def __init__(self, name: str, ingredients: list[str], size: str = 'L'):
        self.name = name
        self.size = size
        self.ingredients = ingredients

    def size_seter(self, size: str):
        """меняет атрибут отвечающий за размер пиццы"""
        if size.upper() not in  {'L', 'XL'}:
            raise ValueError('Данного размера нет в ассортименте')
        self.size = size

    def get_name(self):
        """возвращает название пиццы"""
        return self.name

    def dict(self) -> None:
        """Выводит рецепт в виде словаря"""
        print(self.name, end=': ')
        for i in range(len(self.ingredients)-1):
            print(self.ingredients[i], end=', ')
        print(self.ingredients[-1])


class Hawaiian(PizzaClass):
    def __init__(self, size: str = 'L'):
        self.name = 'Hawaiian \N{Pineapple}'
        self.size = size
        self.ingredients = ['tomato sauce', 'mozzarella', 'chiken', 'pineapples']


class Pepperoni(PizzaClass):
    def __init__(self,  size: str = 'L'):
        self.name = 'Pepperoni \N{Slice of Pizza}'
        self.size = size
        self.ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']


class Margherita(PizzaClass):
    def __init__(self,  size: str = 'L'):
        self.name = 'Margherita \N{Cheese Wedge}'
        self.size = size
        self.ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']