from bun import Bun
import pytest

class TestBun:

    #Проверка наименования
    @pytest.mark.parametrize('name, price', [('ржаная', 1000)])
    def test_name(self, name, price):
        collector = Bun(name=name, price=price)
        assert collector.get_name() == 'ржаная'

    #Проверка цены
    @pytest.mark.parametrize('name, price', [('ржаная', 1000)])
    def test_price(self, name, price):
        collector = Bun(name=name, price=price)
        assert collector.get_price() == 1000
