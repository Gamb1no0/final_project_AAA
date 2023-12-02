import click
from pizzaclass import PizzaClass

# создаем группу команд `cli`

recipes = {
    'Margherita \N{Cheese Wedge}': ['tomato sauce', 'mozzarella', 'tomatoes'],
    'Pepperoni \N{Slice of Pizza}': ['tomato sauce', 'mozzarella', 'pepperoni'],
    'Hawaiian \N{Pineapple}': ['tomato sauce', 'mozzarella', 'chiken', 'pineapples']
}

margherita = PizzaClass('Margherita \N{Cheese Wedge}',
                        ['tomato sauce', 'mozzarella', 'tomatoes'])
pepperoni = PizzaClass('Pepperoni \N{Slice of Pizza}',
                       ['tomato sauce', 'mozzarella', 'pepperoni'])
hawaiian = PizzaClass('Hawaiian \N{Pineapple}',
                      ['tomato sauce', 'mozzarella', 'chiken', 'pineapples'])


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand:
        return
    print()
    print('!!!cli function works!!!')
    print()


@cli.command()
@click.option('--size',
              default='L',
              type=click.Choice(['L', 'XL'], case_sensitive=False))
# show_default добавил
@click.option('--delivery', default=False, is_flag=True, show_default=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    if delivery:
        pass
    """Готовит и доставляет пиццу"""


@cli.command()
def menu():
    margherita.dict()
    pepperoni.dict()
    hawaiian.dict()


if __name__ == '__main__':
    cli()
