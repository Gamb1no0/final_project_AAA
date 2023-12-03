import click
import random
from pizzaclass import PizzaClass

def bake() -> None:
    '''Выводит время приготовления пиццы,
    являющеся случайным числом от 1 до 10
    '''
    rand_num = random.randrange(1, 10)
    print(f'👨‍🍳 Приготовили за {rand_num}с!')


def bake_and_delivery(bake):
    """Декоратор добавляет функционал
    доставки
    """
    def wrapper():
        bake()
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
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, size: str):
    '''команда для заказа пиццы'''

    if pizza not in {'margherita', 'pepperoni', 'hawaiian'}:
        raise ValueError('Такой пиццы нет в ассортименте')
    if size not in {'L', 'XL'}:
        raise ValueError('Такого размера нет в ассортименте')
    
    if delivery:
        bake_delivery = bake_and_delivery(bake)
        bake_delivery()
    else:
        bake()

@cli.command()
def menu():
    margherita.dict()
    pepperoni.dict()
    hawaiian.dict()

if __name__ == '__main__':
    margherita = PizzaClass('Margherita \N{Cheese Wedge}',
                            ['tomato sauce', 'mozzarella', 'tomatoes'])
    pepperoni = PizzaClass('Pepperoni \N{Slice of Pizza}',
                           ['tomato sauce', 'mozzarella', 'pepperoni'])
    hawaiian = PizzaClass('Hawaiian \N{Pineapple}',
                          ['tomato sauce', 'mozzarella', 'chiken', 'pineapples'])
    cli()