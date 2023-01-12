import pytest
from pydantic import ValidationError

from main import show_parse_data


from parse_data import result_data


def test_func_show_correct_data():
    a = show_parse_data(result_data)
    assert a == 1
