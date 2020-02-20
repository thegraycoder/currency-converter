import requests


def get_conversion(base, query, amount):
    """
    Call exchange rate API and get conversion

    :param base: currency to convert from
    :param query: currency to convert to
    :param amount: amount to convert
    :return:
    """
    url = f"https://api.exchangeratesapi.io/latest?base={base}"
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()['rates'][query]) * float(amount)

