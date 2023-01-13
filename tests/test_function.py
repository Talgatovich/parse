from main import show_parse_data
from parse_data import result_data
import pytest

def test_func_show_correct_result(result):
    """Функция выдаёт корректный результат"""
    a = show_parse_data(result_data)
    assert a == result, "Проверьте выходные данные"


def test_data():
   pass

