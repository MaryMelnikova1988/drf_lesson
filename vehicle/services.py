import requests
from rest_framework import status

from config import settings

# https://app.currencyapi.com/dashboard
def convert_currencies(rub_price):
    usd_price = 0
    response = requests.get(
        f'{settings.CUR_API_URL}v3/latest?apikey={settings.CUR_API_KEY}&currencies=RUB'
    )
    # print(response)
    if response.status_code == status.HTTP_200_OK:
        # print(response.json())
        usd_rate = response.json()['data']['RUB']['value']
        # print(usd_rate)
        usd_price = rub_price * usd_rate

    return usd_price
