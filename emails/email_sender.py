from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get credentials from emailaccountdetails.txt
emailaccountdetails = open(
    "/Users/jopderidder/Documents/bitcoin-pricetracker/secret_files/emailaccountdetails.txt", "r")

HOST = emailaccountdetails.readline().strip()
PORT = emailaccountdetails.readline().strip()
ADRES = emailaccountdetails.readline().strip()
PASSWORD = emailaccountdetails.readline().strip()

emailaccountdetails.close()

# # setup the SMTP server
s = smtplib.SMTP(host=HOST, port=PORT)
s.starttls()
s.login(ADRES, PASSWORD)


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def send_email(user_name, current_bitcoin_price, buying_price=None, selling_price=None):
    msg = MIMEMultipart()       # create a message

    # If buying price is not None the buying email will be send, else the selling mail will be send
    if buying_price:
        message = read_template('/Users/jopderidder/Documents/bitcoin-pricetracker/emails/buying_email.txt').substitute(
            NAME=user_name, CURRENT_BITCOIN_PRICE=current_bitcoin_price, BUYING_PRICE=buying_price)
        subject = f'Hi {user_name}, Buy Bitcoins now!'
    else:
        message = read_template('/Users/jopderidder/Documents/bitcoin-pricetracker/emails/selling_email.txt').substitute(
            NAME=user_name, CURRENT_BITCOIN_PRICE=current_bitcoin_price, SELLING_PRICE=selling_price)
        subject = f'Hi {user_name}, Sell your Bitcoins now!'

    # setup the parameters of the message
    msg['From'] = ADRES
    msg['To'] = ADRES
    msg['Subject'] = subject
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg
