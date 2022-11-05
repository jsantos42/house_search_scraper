# Sources:
# https://www.geeksforgeeks.org/pattern-matching-python-regex/
# https://www.thepythoncode.com/article/reading-emails-in-python

import os
from dotenv import load_dotenv
import imaplib
import ssl
import email
from email.header import decode_header
import re


def get_house_url(email_body):
	pattern = re.compile(r'https://www\.casa\.it/immobili/\d*')
	return pattern.findall(email_body)[0]


def get_header_data(email_msg, key):
	value, encoding = decode_header(email_msg[key])[0]
	if isinstance(value, bytes):
		value = value.decode(encoding)
	return value


def init_connection(email_address, password):
	context = ssl.create_default_context()
	imap = imaplib.IMAP4_SSL('imap-mail.outlook.com', ssl_context=context)
	imap.login(email_address, password)
	return imap


def get_user_data():
	load_dotenv()
	return [os.getenv('EMAIL_ADDRESS'), os.getenv('EMAIL_PASSWORD')]


if __name__ == "__main__":
	user, secret = get_user_data()
	connection = init_connection(user, secret)
	mailbox = 'CasaIT'
	msg_count = int(connection.select(mailbox=mailbox)[1][0])
	for i in range(msg_count, 0, -1):
		msg = connection.fetch(str(i), "(RFC822)")[1][0]
		msg = email.message_from_bytes(msg[1])
		subject = get_header_data(msg, "Subject")
		sender = get_header_data(msg, "From")
		body = msg.get_payload(decode=True).decode()
		url = get_house_url(body)
		# now scrape the url (ex: 'https://www.casa.it/immobili/45454130' )
	connection.close()
	connection.logout()
