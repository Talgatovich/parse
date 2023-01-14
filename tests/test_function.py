from main import show_parse_data
from parse_data import result_data


def test_func_show_correct_result(result):
    """Функция выдаёт корректный результат"""
    output = show_parse_data(result_data)
    assert output == result, "Проверьте выходные данные"

