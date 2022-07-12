from ..data.data import Color, Person
from faker import Faker
import random

faker = Faker('ru_Ru')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker.first_name() + " " + faker.last_name(),
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker.job(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address(),
        mobile=faker.msisdn()
    )


def generated_file():
    path = rf'G:\Projects\automation_QA\automation_qa_case\data\filetest{random.randint(0,999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0,999)}')
    file.close
    return file.name, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple",
                    "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )
