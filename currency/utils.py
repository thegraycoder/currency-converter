import requests


def get_conversion(base, query, amount):
    url = f"https://api.exchangeratesapi.io/latest?base={base}"
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()['rates'][query]) * float(amount)

