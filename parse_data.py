from models import Experience
import json

with open('data.json', encoding="UTF-8") as file:
    data = json.load(file)

# Полный адрес
address = data.get("address").get("value")

# Контакты
contacts = data.get("contacts")
name = contacts.pop("fullName")
contacts['name'] = name

# Координаты
coordinates = {
    "latitude": data.get("address").get("lat"),
    "longitude": data.get("address").get("lng")
}

# Зарплата
salary = data.get("salary").get("to")

# Зарплатная вилка
salary_range = {
    "from": data.get("salary").get("from"),
    "to": data.get("salary").get("to")
}

# График работы
schedule = {
    "id": data.get("employment")
}

# Описание
description = data.get("description")

# Должность
name = data.get("name")

# URL изображения
image_url = data.get("image_url", "https://img.hhcdn.ru/employer-logo/3410666.jpeg")

# Опыт работы
experience = data.get("experience", Experience())

billing_type = data.get("billing_type", "packageOrSingle")
business_area = data.get("business_area", 1)
html_tags = data.get("html_tags", True)
allow_messages = data.get("allow_messages", True)

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
    "salary_range": salary_range,
    "image_url": image_url,
    "billing_type": billing_type,
    "business_area": business_area,
    "html_tags": html_tags,
    "allow_messages": allow_messages,

}
