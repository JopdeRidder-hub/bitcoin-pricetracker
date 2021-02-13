from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://bitcoin.nl/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Get the current Bitcoin price
CURRENT_PRICE = soup.findAll("span", {"id": "lastPrice"})[0].get_text()

"""
1. I want to setup the notification sender that can send emails to the users email adress.
2. I want to know the price at which point the notification of selling needs to be send.
3. 
"""


class SellNotification:

    def __init__(self, email, sell_price):
        self.email = email
        self.sell_price = sell_price

    def current_bitcoin_value(self):
        return CURRENT_PRICE
