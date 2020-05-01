import imaplib , email
from bs4 import BeautifulSoup
import os
import mimetypes
username = 'cvidit769@gmail.com'
passw = 'fresh@123'
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username,passw)
def G1():
    mail.select("inbox")
    # create folder
    # mail.create("Item2")
    # mail.list()
    result, data = mail.uid('search', None, "All")
    inbox_item_list = data[0].split()
    for item in inbox_item_list:
        result2, email_data = mail.uid('fetch', item, '(RFC822)')
        raw_email = email_data[0][1].decode("utf-8")
        email_message = email.message_from_string(raw_email)
        aa = email_message['To']
        qq = email_message['From']
        ww = email_message['Subject']
        ss = email_message['Date']
        counter = 1
        for part in email_message.walk():

            if part.get_content_maintype() == "multipart":
                continue
            filename = part.get_filename()
            if not filename:
                ext = '.html'
                filename = 'msg-part-%08d%s' % (counter, ext)
            counter += 1
            """
            save file
            """
            content_type = part.get_content_type()
            #print("S.N.O:=>", counter)
            #print("To:=>", aa)
            #print("From:=>", qq)
            #print("Subject:=>", ww)
            #print("Date:=>", ss)
            #print("Content Type :=>", content_type)
            if "plain" in content_type:
                print("S.N.O:=>", counter)
                print("To:=>", aa)
                print("From:=>", qq)
                print("Subject:=>", ww)
                print("Date:=>", ss)
                print("Content Type :=>", content_type)
                print(part.get_payload())
            elif "html" in content_type:
                print("S.N.O:=>", counter)
                print("To:=>", aa)
                print("From:=>", qq)
                print("Subject:=>", ww)
                print("Date:=>", ss)
                print("Content Type :=>", content_type)
                html_ = part.get_payload()
                soup = BeautifulSoup(html_, "html.parser")
                text = soup.get_text()
                print(text)
            else:
                print(content_type)

G1()
