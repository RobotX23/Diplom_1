from praktikum.database import Database
from praktikum.ingredient_types import *

class TestDatebase:


    #Проверка количества булок
    def test_bun(self):
        collector = Database()
        assert len(collector.available_buns()) == 3

    #Проверка стоимости булок
    def test_bun_price(self):
        summ = 0
        collector = Database()
        bun = collector.available_buns()
        for i in range(len(collector.available_buns())):
            summ = bun[i].get_price() + summ
        assert summ == 600

    #Проверка доступного наименование булок
    def test_bun_name(self):
        name = []
        collector = Database()
        bun = collector.available_buns()
        for i in range(len(collector.available_buns())):
            name.append(bun[i].get_name())
        assert name == ["black bun", "white bun", "red bun"]

    #Проверка количества ингредиентов
    def test_ingredients(self):
        collector = Database()
        assert len(collector.available_ingredients()) == 6

    #Проверка стоимости ингредиентов
    def test_ingredients_price(self):
        summ = 0
        collector = Database()
        ingredients = collector.available_ingredients()
        for i in range(len(collector.available_ingredients())):
            summ = ingredients[i].get_price() + summ
        assert summ == 1200

    #Проверка наименования соусов
    def test_ingredients_name_sauce(self):
        name = []
        collector = Database()
        ingredients = collector.available_ingredients()
        for i in range(len(collector.available_ingredients())):
            if ingredients[i].get_type() == INGREDIENT_TYPE_SAUCE:
                name.append(ingredients[i].get_name())
        assert name == ["hot sauce", "sour cream", "chili sauce"]

    #Проверка наименования заполнения
    def test_ingredients_name_filling(self):
        name = []
        collector = Database()
        ingredients = collector.available_ingredients()
        for i in range(len(collector.available_ingredients())):
            if ingredients[i].get_type() == INGREDIENT_TYPE_FILLING:
                name.append(ingredients[i].get_name())
        assert name == ["cutlet", "dinosaur", "sausage"]