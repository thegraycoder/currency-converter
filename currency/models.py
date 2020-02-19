from django.db import models

CURRENCY_CHOICES = [
    'USD',
    'EUR',
    'JPY'
]


def human_readable(value):
    if value == 'USD':
        return 'US Dollars'
    if value == 'EUR':
        return 'EURO'
    if value == 'JPY':
        return 'Japanese Yen'
