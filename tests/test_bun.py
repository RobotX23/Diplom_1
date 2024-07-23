from praktikum.bun import Bun
import pytest
from data import *

class TestBun:

    #Проверка наименования
    @pytest.mark.parametrize('name, price', [(BUN[0], BUN[1])])
    def test_name(self, name, price):
        collector = Bun(name=name, price=price)
        assert collector.get_name() == 'ржаная'

    #Проверка цены
    @pytest.mark.parametrize('name, price', [(BUN[0], BUN[1])])
    def test_price(self, name, price):
        collector = Bun(name=name, price=price)
        assert collector.get_price() == 1000
