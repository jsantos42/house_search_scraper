import email
import re
from scraper import scrape_urls


def get_house_urls(email_body, pattern):
    pattern = re.compile(pattern)
    urls_list = []
    [urls_list.append(x) for x in re.findall(pattern, email_body) if x not in urls_list]
    return urls_list


def check_mailbox(imap, website):
    msg_count = int(imap.select(mailbox=website['mailbox'])[1][0])
    urls = []
    for i in range(msg_count, 0, -1):
        msg = imap.fetch(str(i), "(RFC822)")[1][0]
        msg = email.message_from_bytes(msg[1])
        body = msg.get_payload(decode=True).decode()
        [urls.append(x) for x in get_house_urls(body, website['url_pattern']) if x not in urls]
    scrape_urls(urls, website)
    imap.close()
    imap.logout()
