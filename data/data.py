
from calendar import month
from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname:  str = None
    email: str = None
    age: int = None
    salary: int = None
    mobile: str = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None


@dataclass
class Color:
    color_name: list = None


@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None
