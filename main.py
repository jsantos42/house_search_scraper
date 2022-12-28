import json
import os
from dotenv import load_dotenv
import ssl
import imaplib
from read_email import check_mailbox


def read_config():
	try:
		with open('config.json') as config_file:
			return json.load(config_file)['websites']
	except FileNotFoundError as err:
		print(err)
		exit(1)


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
	config_data = read_config()
	check_mailbox(connection, config_data['casa_it'])
