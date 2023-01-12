from models import *
import json

with open('data.json', encoding="UTF-8") as f:
    data = json.load(f)

address = data["address"]["value"]
contacts = data["contacts"]
coordinates = {
    "latitude": data["address"]["lat"],
    "longitude": data["address"]["lng"]
}

salary = data["salary"]["to"]

salary_range = {
    "from": data["salary"]["from"],
    "to": data["salary"]["to"]
}
description = data["description"]
name = data["name"]
schedule = Schedule()
experience = Experience()

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
