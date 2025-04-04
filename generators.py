from faker import Faker
from random import randint

fake = Faker('ru_RU')


def fake_data():
    name = fake.first_name_male()
    surname = fake.last_name_male()
    return name, surname


def fake_phone():
    return f'89{randint(100000000, 999999999)}'
