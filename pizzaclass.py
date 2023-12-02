class PizzaClass:
    def __init__(self, name: str, ingredients: list[str], size: str = 'L'):
        # если размер или название не подходящие
        # вроде это можно сделтаь через консольные команды
        self.name = name
        self.size = size
        self.ingredients = ingredients

    def dict(self) -> None:
        '''Выводит рецепт в виде словаря'''

        print(self.name, end=': ')
        for i in range(len(self.ingredients)-1):
            print(self.ingredients[i], end=', ')
        print(self.ingredients[-1])

    # def pizza_size_setter(pizza_size: str) -> None:
    #     if pizza_size not in {'L', 'XL'}
