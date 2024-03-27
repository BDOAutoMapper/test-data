from faker import Faker
import random
import datetime


def create_faker() -> Faker:
    return Faker()


faker = create_faker()


def fake_int(min: int = int(1e8), max: int = int(1e9)) -> int:
    return faker.random_int(min=min, max=max)


def boekstuk() -> datetime.date:
    random_days = random.randint(1, 365)
    past_date = datetime.datetime.now() - datetime.timedelta(days=random_days)
    return past_date.date()


def vervalt() -> datetime.date:
    return datetime.date.today()


def name() -> str:
    return faker.name()


def factuurnummer(min: int = int(1e8), max: int = int(1e9)) -> int:
    """
    Generate a random invoice number within the specified range.

    Args:
        min (int, optional): The minimum value of the invoice number (inclusive). Defaults to 100000000.
        max (int, optional): The maximum value of the invoice number (inclusive). Defaults to 1000000000.

    Returns:
        int: A randomly generated 8-digit invoice number. As defined by the sample data.
    """
    num = faker.random_int(min=min, max=max)
    return num


def debnummer(min: int = 1_000, max: int = 9_999) -> int:
    """
    Generate a random debtor number within the specified range.

    Args:
        min (int, optional): The minimum value of the debtor number (inclusive). Defaults to 1000.
        max (int, optional): The maximum value of the debtor number (inclusive). Defaults to 9999.

    Returns:
        int: A randomly generated 4-digit debtor number. As defined by the sample data.
    """
    num = faker.random_int(min=min, max=max)
    return num


def factuur(min: float = 0, max: float = 10_000, decimal_places: int = 2) -> float:
    sum = round(random.uniform(min, max), decimal_places)
    return sum


def iban(country_code: str = "NL") -> str:
    checksum = faker.random_number(digits=2)
    bank_code = faker.random_number(digits=4)
    account_num = faker.random_number(digits=10)
    iban = f"{country_code}{checksum}{bank_code}{account_num}"
    return iban


def factuurstatus() -> str:
    """
    Generate a random payment status.

    Returns:
        str: A randomly chosen payment status from the list of options as listed in the sample data. 
    """
    payment_statuses = ["Wacht op betaling debiteur", "Niet vervallen"]
    return random.choice(payment_statuses)


def omschrijving() -> str:
    """
    Generate a random description.

    Returns:
        str: A string representing a random description consisting of a word followed by a random date.
        From the sample data: Zorgverzekeringswet - 2023-12-01 / 2023-12-31

    """
    random_str = faker.word()
    random_date = faker.date()
    out = f"{random_str} {random_date}"
    return out
