from praktikum.burger import Burger
import pytest
from data import *
from unittest.mock import Mock




class TestBurger():


    #Проверка добавления булки
    @pytest.mark.parametrize('name, price', [(BUN[0], BUN[1])])
    def test_set_buns(self, name, price):
        collector = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = name
        mock_bun.get_price.return_value = price
        collector.set_buns(mock_bun)
        assert collector.bun == mock_bun

    #Проверка добавление ингридиенат
    @pytest.mark.parametrize('ingredient_type ,name, price', [(POTATO[0], POTATO[1], POTATO[2])])
    def test_add_ingredient(self, name, price, ingredient_type):
        collctor = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        mock_ingredient.get_type.return_value = ingredient_type
        collctor.add_ingredient(mock_ingredient)
        assert collctor.ingredients[0].get_price() == POTATO[2] and collctor.ingredients[0].get_name() == POTATO[1] and collctor.ingredients[0].get_type() == POTATO[0]

    #Проверка удаление ингридиентов
    @pytest.mark.parametrize('ingredient_type ,name, price', [(POTATO[0], POTATO[1], POTATO[2])])
    def test_remove_ingredient(self, ingredient_type, name, price):
        collctor = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        mock_ingredient.get_type.return_value = ingredient_type
        collctor.add_ingredient(mock_ingredient)
        collctor.remove_ingredient(0)
        assert len(collctor.ingredients) == 0

    #Проверка перемещение ингридиента
    @pytest.mark.parametrize('ingredient_1 ,ingredient_2', [(POTATO, KETCHUP)])
    def test_move_ingredient(self, ingredient_1 ,ingredient_2):
        collctor = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_name.return_value = ingredient_1[1]
        mock_ingredient_1.get_price.return_value = ingredient_1[2]
        mock_ingredient_1.get_type.return_value = ingredient_1[0]
        collctor.add_ingredient(mock_ingredient_1)
        mock_ingredient_1.get_name.return_value = ingredient_2[1]
        mock_ingredient_1.get_price.return_value = ingredient_2[2]
        mock_ingredient_1.get_type.return_value = ingredient_2[0]
        collctor.add_ingredient(mock_ingredient_1)
        collctor.move_ingredient(1, 0)
        assert collctor.ingredients[0].get_price() == ingredient_2[2] and collctor.ingredients[0].get_name() == ingredient_2[1] and collctor.ingredients[0].get_type() == ingredient_2[0]

    #Проверка стоимости бургера
    @pytest.mark.parametrize('BUN, ingredient', [(BUN, POTATO)])
    def test_get_price(self, BUN, ingredient):
        collector = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = BUN[0]
        mock_bun.get_price.return_value = BUN[1]
        collector.set_buns(mock_bun)
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = ingredient[1]
        mock_ingredient.get_price.return_value = ingredient[2]
        mock_ingredient.get_type.return_value = ingredient[0]
        collector.add_ingredient(mock_ingredient)
        assert collector.get_price() == (2*BUN[1] + ingredient[2])

    #Проверка получение чека
    @pytest.mark.parametrize('BUN, ingredient', [(BUN, POTATO)])
    def test_get_receipt(self, BUN, ingredient):
        collector = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = BUN[0]
        mock_bun.get_price.return_value = BUN[1]
        collector.set_buns(mock_bun)
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = ingredient[1]
        mock_ingredient.get_price.return_value = ingredient[2]
        mock_ingredient.get_type.return_value = ingredient[0]
        collector.add_ingredient(mock_ingredient)
        recept = '(==== ржаная ====)\n= filling картошка =\n(==== ржаная ====)\n\nPrice: 2099.1'
        assert collector.get_receipt() == recept