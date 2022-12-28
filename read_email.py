import email
from email.header import decode_header
import re


def get_house_urls(email_body, pattern):
    pattern = re.compile(pattern)
    urls_list = []
    [urls_list.append(x) for x in re.findall(pattern, email_body) if x not in urls_list]
    print(urls_list)
    return urls_list


def get_header_data(email_msg, key):
    value, encoding = decode_header(email_msg[key])[0]
    if isinstance(value, bytes):
        value = value.decode(encoding)
    return value


def check_mailbox(imap, website):
    msg_count = int(imap.select(mailbox=website['mailbox'])[1][0])
    for i in range(msg_count, 0, -1):
        msg = imap.fetch(str(i), "(RFC822)")[1][0]
        msg = email.message_from_bytes(msg[1])
        subject = get_header_data(msg, "Subject")
        sender = get_header_data(msg, "From")
        body = msg.get_payload(decode=True).decode()
        urls = get_house_urls(body, website['url_pattern'])
    # now scrape the urls (ex: 'https://www.casa.it/immobili/45454130' )
    # read from config.json
    imap.close()
    imap.logout()

    # with open('body.txt') as file:
    #     urls = get_house_urls(file.read())
    #     print(urls)
