from click.testing import CliRunner
import unittest
import random
from cli import order
from cli import menu

#Ставлю сид, чтобы было удобнее тестить
random = random.Random(42)

class CliOrderTests(unittest.TestCase):

    def test_menu(self):
        runner = CliRunner()
        result = runner.invoke(menu)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, 'Margherita 🧀: tomato sauce, mozzarella, tomatoes\n'
                         + 'Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n'
                         + 'Hawaiian 🍍: tomato sauce, mozzarella, chiken, pineapples\n')

    def test_order_pizza_upper1(self):
        runner = CliRunner()
        result = runner.invoke(order, ['Margherita'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, '👨‍🍳 приготовили за 7с!\n')

    def test_order_pizza_upper2(self):
        runner = CliRunner()
        result = runner.invoke(order, ['PePPeroni'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, '👨‍🍳 приготовили за 1с!\n')

    def test_order_pizza_upper3(self):
        runner = CliRunner()
        result = runner.invoke(order, ['HAWAIIAN'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, '👨‍🍳 приготовили за 1с!\n')

    def test_order_pizza_lower(self):
        runner = CliRunner()
        result = runner.invoke(order, ['margherita'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, '👨‍🍳 приготовили за 4с!\n')
    
    def test_order_pizza_unknown(self):
        runner = CliRunner()
        result = runner.invoke(order, ['ASDsaf'])
        self.assertEqual(result.exit_code, 1)
        self.assertEqual(result.output, 'Такой пиццы нет в ассортименте\n')
    
    def test_order_pizza_deliver1(self):
        runner = CliRunner()
        result = runner.invoke(order, ['margherita', '--delivery'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, '👨‍🍳 приготовили за 2с!\n'
                         + 'Курьер взял пиццу Margherita 🧀\n'
                         + '🛵 Доставили за 1c!\n')
        
    def test_order_pizza_deliver2(self):
        runner = CliRunner()
        result = runner.invoke(order, ['PePPeroni', '--delivery'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, '👨‍🍳 приготовили за 5с!\n'
                         + 'Курьер взял пиццу Pepperoni 🍕\n'
                         + '🛵 Доставили за 4c!\n')
        
    def test_order_pizza_size1(self):
        runner = CliRunner()
        result = runner.invoke(order, ['Pepperoni', '--size', 'L'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, '👨‍🍳 приготовили за 3с!\n')

    def test_order_pizza_size2(self):
        runner = CliRunner()
        result = runner.invoke(order, ['Pepperoni', '--size', 'XL'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, '👨‍🍳 приготовили за 2с!\n')
        
    def test_order_pizza_wrong_size(self):
        runner = CliRunner()
        result = runner.invoke(order, ['pepperoni', '--size', 'LSDSL'])
        self.assertEqual(result.exit_code, 2)
        self.assertEqual(result.output, 'Такого размера нет в ассортименте\n')
    
    def test_order_pizza_wrong_pizza_wrong_size(self):
        runner = CliRunner()
        result = runner.invoke(order, ['peponi', '--size', 'LSDSL'])
        self.assertEqual(result.exit_code, 1)
        self.assertEqual(result.output, 'Такой пиццы нет в ассортименте\n')
    
    def test_order_pizza_size_deliver(self):
        runner = CliRunner()
        result = runner.invoke(order, ['margherita', '--size', 'L', '--delivery'])
        self.assertEqual(result.exit_code, 0)

