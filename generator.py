from faker import Faker
import random
import datetime

def create_faker() -> Faker:
    return Faker()

faker = create_faker()

def fake_int(min: int = int(1e8), max: int = int(1e9)) -> int:
    return faker.random_int(min=min, max=max)

    
def boekstuk() -> datetime.datetime:
    return datetime.datetime.now()
    
def name() -> str:
    return faker.name()

# old method of generating factuur, debituur nr
def factuurnummer(min: int = int(1e8), max: int = int(1e9)) -> int:
    num = faker.random_int(min=min, max=max)
    return num

def debnummer(min: int = 1_000, max: int = 9_999) -> int:
    num = faker.random_int(min=min, max=max)
    return num

def factuur(min: float = 0, max: float = 10_000, decimal_places: int = 2) -> float:
    sum = round(random.uniform(min, max), decimal_places)
    return sum