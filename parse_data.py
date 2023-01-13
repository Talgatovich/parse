from models import *
import json

with open('data.json', encoding="UTF-8") as f:
    data = json.load(f)

# Полный адрес
address = data["address"]["value"]

# Контакты
contacts = data["contacts"]
name = contacts.pop("fullName")
contacts['name'] = name

# Координаты
coordinates = {
    "latitude": data["address"]["lat"],
    "longitude": data["address"]["lng"]
}

# Зарплата
salary = data["salary"]["to"]

# Зарплатная вилка
salary_range = {
    "from": data["salary"]["from"],
    "to": data["salary"]["to"]
}

# Описание
description = data["description"]
name = data["name"]
schedule = Schedule()
experience = Experience()

# Результирующий список
result_data = {
    "address": address,
    "contacts": contacts,
    "coordinates": coordinates,
    "description": description,
    "name": name,
    "salary": salary,
    "schedule": schedule,
    "experience": experience,
    "salary_range": salary_range
}
