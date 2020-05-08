# Unittest provides a test runner that you can use by typing python -m unittest in your
# terminal. When you run the unittest test runner, it will look for tests by
# 1 Looking in the current directory (and any subdirectories) for modules named
# test_* or *_test
# 2 Looking in those modules for classes that inherit from unittest.TestCase
# 3 Looking in those classes for methods that start with test_

#example
class Product:
    def __init__(self, name, size, color):
        self.name = name 
        self.size = size 
        self.color = color 

    def transform_name_for_sku(self):
        return self.name.upper()

    def transform_color_for_sku(self):
        return self.color.upper()

    def generate_sku(self):
        name = self.transform_name_for_sku()
        color = self.transform_color_for_sku()
        return f'{name}-{self.size}-{color}'

import unittest

class ProductTestCase(unittest.TestCase):
    def test_transform_name_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = 'SHOES'
        actual_value = small_black_shoes.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value) 

#python3 -m unittest

### Integration test
from collections import defaultdict

class ShoppingCart:
    def __init__(self):
        self.products = defaultdict(lambda: defaultdict(int))

    def add_product(self, product, quantity = 1):
        self.products[product.generate_sku()]['quantity'] += quantity

    def remove_product(self, product, quantity=1):
        sku = product.generate_sku()
        self.products[sku]['quantity'] -= quantity
        if self.products[sku]['quantity'] <= 0:
            del self.products[sku]

class ShoppingCartTestCase(unittest.TestCase):
    def test_add_and_remove_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product)
        cart.remove_product(product)

        self.assertEqual({}, cart.products)

from urllib.request import urlopen

def add_sales_tax(original_amount, country, region):
    sales_tax_rate = urlopen(f'https://tax-api.com/{country}/{region}').read().decode()
    return original_amount * float(sales_tax_rate)

#A unit test with mocking 
import io
from unittest import mock 

class SaleTaxTestCase(unittest.TestCase):
    @mock.patch('testing.urlopen') # testing is the module name
    def test_get_sales_tax_returns_proper_value_from_api(
        self, mock_urlopen):
        test_tax_rate = 1.06
        mock_urlopen.return_value = io.BytesIO(str(test_tax_rate).encode('utf-8'))
        self.assertEqual(5 * test_tax_rate, add_sales_tax(5, 'USA', 'MI'))

#testing suite for Product and ShoppingCart
class ProductTestCase(unittest.TestCase):
    def test_transform_name_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual('SHOES', small_black_shoes.transform_name_for_sku())

    def test_transform_color_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual('BLACK', small_black_shoes.transform_color_for_sku())

    def test_generate_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual('SHOES-S-BLACK', small_black_shoes.generate_sku())

class ShoppingCartTestCase(unittest.TestCase):
    def test_cart_initial_empty(self):
        cart = ShoppingCart()
        self.assertDictEqual({}, cart.products)

    def test_add_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product)
        self.assertDictEqual({'SHOES-S-BLUE': {'quantity': 1}}, cart.products)

    def test_add_two_of_a_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product, quantity=2)
        self.assertDictEqual({'SHOES-S-BLUE': {'quantity': 2}}, cart.products)

    def test_add_two_different_products(self):
        cart = ShoppingCart()
        product_one = Product('shoes', 'S', 'blue')
        product_two = Product('shirt', 'M', 'gray')

        cart.add_product(product_one)
        cart.add_product(product_two)

        self.assertDictEqual(
            {
                'SHOES-S-BLUE': {'quantity': 1},
                'SHIRT-M-GRAY': {'quantity': 1}
            },
            cart.products
        )

    def test_add_and_remove_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product)
        cart.remove_product(product)

        self.assertDictEqual({}, cart.products)

    def test_remove_too_many_products(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product)
        cart.remove_product(product, quantity=2)

        self.assertDictEqual({}, cart.products)

#Transform to Pytest:
#No need to inherit from any base case
#self.assertEqual goes away; uses raw assert statements instead

