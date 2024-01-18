import click
import random
from typing import Union
from pizzaclass import Hawaiian
from pizzaclass import Pepperoni
from pizzaclass import Margherita

#Ставлю сид, чтобы было удобнее тестить
random = random.Random(42)

MENU = {
        'margherita':
           Margherita,
        'pepperoni':
            Pepperoni,
        'hawaiian':
            Hawaiian
}


def log(template):
    """Декоратор имитирует логирование
    времени работы функции"""
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            rand_num = random.randrange(1, 10)
            output = template.format(rand_num)
            click.echo(output)
            return result
        return wrapper
    return decorator


@log('👨‍🍳 приготовили за {}с!')
def bake(pizza_nm: str, size: str) -> Union[Hawaiian, Pepperoni, Margherita]:
    """Готовит пиццу"""
    return MENU[pizza_nm](size)


@log('🛵 Доставили за {}c!')
def deliver(pizza: Union[Hawaiian, Pepperoni, Margherita]) -> None:
    """Сообщает, что курьер забрал пиццу"""
    click.echo(f'Курьер взял пиццу {pizza.get_name()}')


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand:
        return


@cli.command()
@click.option('--size', default='L',
              help = 'L|XL',
              show_default=True)
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza_nm', nargs=1)
def order(pizza_nm: str, delivery: bool, size: str):
    """команда для заказа пиццы"""

    pizza_nm = pizza_nm.lower()
    if pizza_nm not in {'margherita', 'pepperoni', 'hawaiian'}:
        click.echo('Такой пиццы нет в ассортименте')
        exit(1)
    if size not in {'L', 'XL'}:
        click.echo('Такого размера нет в ассортименте')
        exit(2)

    pizza = bake(pizza_nm, size)
    if delivery:
        deliver(pizza)


@cli.command()
def menu():
    """команда для показа меню пиццерии"""
    for classes in MENU.values():
        temp_pizza = classes()
        temp_pizza.dict()


if __name__ == '__main__':
    cli()