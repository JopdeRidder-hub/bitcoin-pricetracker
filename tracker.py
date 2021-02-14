from bs4 import BeautifulSoup
from urllib.request import urlopen
from string import Template
from emails import email_sender

# Setup beautifulsoup to extract the current bitcoin price
url = "https://bitcoin.nl/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Get the current Bitcoin price
CURRENT_BITCOIN_PRICE = soup.findAll("span", {"id": "lastPrice"})[0].get_text()

"""
1. I want to setup the notification sender that can send emails to the users email adress.
2. I want to know the price at which point the notification of selling needs to be send.
3. I want to calculate the average bitcoin value.
4. I want to know at what point the user wants to buy and get notified.
"""


class SellNotification:

    def __init__(self, name, selling_price, buying_price):
        self.name = name
        self.selling_price = selling_price
        self.buying_price = buying_price

    def send_email(self):
        if float(self.buying_price) > float(CURRENT_BITCOIN_PRICE[0:6]):
            email_sender.send_email(
                self.name, CURRENT_BITCOIN_PRICE, buying_price=self.buying_price)
        if float(self.selling_price) < float(CURRENT_BITCOIN_PRICE[0:6]):
            email_sender.send_email(
                self.name, CURRENT_BITCOIN_PRICE, selling_price=self.selling_price)


SellNotification(name='Paul', selling_price='40.000',
                 buying_price='29.000').send_email()
