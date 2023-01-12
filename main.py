from pprint import pprint

from pydantic import ValidationError

from parse_data import result_data
from models import Summary


def show_parse_data(data):
    try:
        data = Summary.parse_obj(result_data)
        return data.dict()

    except ValidationError as e:
        return e.json()


if __name__ == "__main__":
    pprint(show_parse_data(result_data))
