import click
import random
from pizzaclass import PizzaClass

MENU = {
        'margherita \N{Cheese Wedge}':
            ['tomato sauce', 'mozzarella', 'tomatoes'],
        'pepperoni \N{Slice of Pizza}':
            ['tomato sauce', 'mozzarella', 'pepperoni'],
        'hawaiian \N{Pineapple}':
            ['tomato sauce', 'mozzarella', 'chiken', 'pineapples']}

def bake(pizza: PizzaClass) -> None:
    """Выводит время приготовления пиццы,
    являющеся случайным числом от 1 до 10
    """

    rand_num = random.randrange(1, 10)
    print(f'👨‍🍳 Приготовили {pizza.name} за {rand_num}с!')


def log(bake):
    """Декоратор добавляет функционал
    доставки"""

    def wrapper(*args):
        print('Имя декорируемой функции - ', bake.__name__)
        bake(*args)
        rand_num = random.randrange(1, 10)
        print(f'🛵 Доставили за {rand_num}c!')
    return wrapper


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand:
        return


@cli.command()
@click.option('--size', default='L',
              help = 'L|XL', show_default=True)
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza_nm', nargs=1)
def order(pizza_nm: str, delivery: bool, size: str):
    """команда для заказа пиццы"""

    if pizza_nm not in {'margherita', 'pepperoni', 'hawaiian'}:
        raise ValueError('Такой пиццы нет в ассортименте')
    if size not in {'L', 'XL'}:
        raise ValueError('Такого размера нет в ассортименте')

    pizza = PizzaClass(pizza_nm, menu[pizza_nm], size)

    if delivery:
        bake_delivery = log(bake)
        bake_delivery(pizza)
    else:
        bake(pizza)


@cli.command()
def menu():
    """команда для показа меню пиццерии"""

    for name, ingredients in MENU.items():
        print(name.capitalize(), end = ':  ')
        for index, elem in enumerate(ingredients):
            if index == len(ingredients) - 1:
                print(elem, end='')
            else:
                print(elem, end=', ')
        print()


if __name__ == '__main__':
    cli()