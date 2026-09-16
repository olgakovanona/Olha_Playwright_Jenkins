import random
from faker import Faker

fake = Faker()


def generate_random_email():
    return fake.email()


def generate_random_phone():
    return f"+31{random.randint(600000000, 699999999)}"


def generate_random_name():
    return fake.company()


def generate_random_address():
    return {
        "street": fake.street_name(),
        "zip": fake.postcode(),
        "city": fake.city(),
        "country": "Netherlands",
        "state": "Noord-Brabant"
    }
