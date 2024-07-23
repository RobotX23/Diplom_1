from praktikum.ingredient import Ingredient
from data import *
import pytest

class TestIngredient():

    @pytest.mark.parametrize('ingredient_type ,name, price', [(POTATO[0], POTATO[1], POTATO[2])])
    def test_price(self, ingredient_type, name, price):
        collector = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert collector.get_price() == 99.10

    @pytest.mark.parametrize('ingredient_type ,name, price', [(KETCHUP[0], KETCHUP[1], KETCHUP[2])])
    def test_name(self, ingredient_type, name, price):
        collector = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert collector.get_name() == 'кетчуп'

    @pytest.mark.parametrize('ingredient_type ,name, price', [(MUSTARD[0], MUSTARD[1], MUSTARD[2])])
    def test_get_type(self, ingredient_type, name, price):
        collector = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert collector.get_type() == 'SAUCE'