from pydantic import BaseModel, Field, validator


class Coordinates(BaseModel):
    """Координаты"""
    latitude: float
    longitude: float


class Phone(BaseModel):
    """Номер телефона"""
    country: str
    city: str
    number: str


class Schedule(BaseModel):
    """График работы"""
    id: str


class Contacts(BaseModel):
    """Контакты"""
    email: str
    name: str = Field()
    phone: Phone | str

    @validator("phone")
    def parse_phone_number(cls, phone):
        country = phone[0:1]
        city = phone[1:4]
        number = phone[4:7] + '-' + phone[7:9] + '-' + phone[9::]
        phone_number = Phone(country=country, city=city, number=number)
        return phone_number


class SalaryRange(BaseModel):
    """Зарплатная вилка"""
    salary_from: int = Field(alias="from")
    salary_to: int = Field(alias="to")


class Experience(BaseModel):
    """Опыт"""
    id: str = "noMatter"


class Summary(BaseModel):
    """Резюме"""
    address: str
    allow_messages: bool
    billing_type: str
    business_area: int
    contacts: Contacts
    coordinates: Coordinates
    description: str
    experience: Experience
    html_tags: bool
    image_url: str
    name: str
    salary: int
    salary_range: SalaryRange
    schedule: Schedule
