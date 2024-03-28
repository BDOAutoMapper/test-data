import pytest
from pathlib import Path
import generator
import datetime

_data_path = Path(__file__).parent / Path("sample_data/sample_input.xlsx")


def test_omschrijving():
    omschrijving = generator.omschrijving()
    assert isinstance(omschrijving, str)
    assert len(omschrijving) > 0


@pytest.mark.parametrize(
    "min_value, max_value", [(1, 10), (100, 1_000), (10_000, 100_000)]
)
def test_factuurnummer(min_value, max_value):
    num = generator.factuurnummer(min_value, max_value)
    assert isinstance(num, int)
    assert min_value <= num <= max_value


@pytest.mark.parametrize(
    "min_value, max_value", [(1, 10), (100, 1_000), (10_000, 100_000)]
)
def test_debnummer(min_value, max_value):
    num = generator.debnummer(min_value, max_value)
    assert isinstance(num, int)
    assert min_value <= num <= max_value


def test_boekstuk():
    past_date = generator.boekstuk()
    today = datetime.date.today()
    assert isinstance(past_date, datetime.date)
    assert past_date < today


def test_vervalt():
    today = generator.vervalt()
    assert isinstance(today, datetime.date)
    assert today == datetime.date.today()


def test_name():
    generated_name = generator.name()
    assert isinstance(generated_name, str)
    assert generated_name.strip() != ""


@pytest.mark.parametrize(
    "min_value, max_value, decimal_places",
    [(0, 10_000, 2), (-100, 100, 1), (500, 1_000, 3)],
)
def test_factuur(min_value, max_value, decimal_places):
    generated_factuur = generator.factuur(min_value, max_value, decimal_places)
    assert isinstance(generated_factuur, float)
    assert min_value <= generated_factuur <= max_value
    assert len(str(generated_factuur).split(".")[1]) == decimal_places


@pytest.mark.parametrize("country_code", ["NL", "DE", "FR"])
def test_iban(country_code):
    generated_iban = generator.iban(country_code)
    assert isinstance(generated_iban, str)
    assert generated_iban.startswith(country_code)
    assert len(generated_iban) <= 34
    assert len(generated_iban) > 5


def test_factuurstatus():
    generated_status = generator.factuurstatus()
    assert isinstance(generated_status, str)
    assert generated_status.strip() != ""
