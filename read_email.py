import email
import re


def get_house_urls(email_body, pattern):
    pattern = re.compile(pattern)
    urls_list = []
    [urls_list.append(x) for x in re.findall(pattern, email_body) if x not in urls_list]
    print(urls_list)
    return urls_list


def check_mailbox(imap, website):
    msg_count = int(imap.select(mailbox=website['mailbox'])[1][0])
    for i in range(msg_count, 0, -1):
        msg = imap.fetch(str(i), "(RFC822)")[1][0]
        msg = email.message_from_bytes(msg[1])
        body = msg.get_payload(decode=True).decode()
        urls = get_house_urls(body, website['url_pattern'])
    imap.close()
    imap.logout()

    # with open('body.txt') as file:
    #     urls = get_house_urls(file.read())
    #     print(urls)
