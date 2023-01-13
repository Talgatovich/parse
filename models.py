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
    id: str = "fullDay"


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
        num = Phone(country=country, city=city, number=number)
        return num


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
    allow_messages: bool = True
    billing_type: str = "packageOrSingle"
    business_area: int = 1
    contacts: Contacts
    coordinates: Coordinates
    description: str
    experience: Experience
    html_tags: bool = True
    image_url: str = "https://img.hhcdn.ru/employer-logo/3410666.jpeg"
    name: str
    salary: int
    salary_range: SalaryRange
    schedule: Schedule
