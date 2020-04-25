import imaplib , email , json
from bs4 import BeautifulSoup
import os
import mimetypes
username = 'hblocks001@gmail.com'
passw = 'jmvherdhmwucxpgn'
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username,passw)
def A():  #list of mail
    mail.select("inbox")
    mail.list()
    print(mail.list())

def B(): # no of mail in inbox
    mail.select("inbox")
    result,data = mail.uid('search',None, "All")
    print(data)
def C():
    mail.select("inbox")
    mail.create("Item2")
    mail.list()
    result, data = mail.uid('search', None, "All")
    inbox_item_list = data[0].split()
    most_recent = inbox_item_list[-1]
    oldest = inbox_item_list[0]
    result2,  email_data = mail.uid('fetch',oldest,'(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    email_message['To']
    email_message['From']
    email_message['Subject']
    email_message.get_payload()


def D():
    mail.select("inbox")
    mail.create("Item2")
    mail.list()
    result, data = mail.uid('search', None, "All")
    inbox_item_list = data[0].split()
    most_recent = inbox_item_list[-1]
    oldest = inbox_item_list[0]

def E():
    mail.select("inbox")
    mail.create("Item2")
    mail.list()
    result, data = mail.uid('search', None, "All")
    inbox_item_list = data[0].split()
    most_recent = inbox_item_list[-1]
    oldest = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', oldest, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    aa=email_message['To']
    qq=email_message['From']
    ww=email_message['Subject']
    print(aa)
    print(qq)
    print(ww)

def F():
    mail.select("inbox")
    #create folder
    #mail.create("Item2")
    #mail.list()
    result, data = mail.uid('search', None, "All")
    inbox_item_list = data[0].split()
    for item in inbox_item_list:
        result2, email_data = mail.uid('fetch',item, '(RFC822)')
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
           filename =  part.get_filename()
           content_type = part.get_content_type()
           if not filename:

                exe = mimetypes.guess_extension(content_type )
                if not exe:
                    exe = ".bin"
                filename = 'msg-part-%08d%s' %(counter,exe)
           counter +=1
                 # save file

        save_path = os.path.join("F:","emails",ss,ww)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        with open(os.path.join(save_path,filename),'wb') as fp :
            fp.write(part.get_payload(decode=True))




        if "plain" in content_type:
            print(part.get_payload())
        elif "html" in content_type:
            html_= part.get_payload()
            soup = BeautifulSoup(html_,"html.parser")
            text = soup.get_text()
            print(text)
        else :
            print(content_type)
        #email_message.get_payload()

def G():
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
                filename = 'msg-part-%08d%s' %(counter,ext)
            counter += 1
            """
            save file
            """
            content_type = part.get_content_type()
            print("S.N.O:=>",counter)
            print("To:=>",aa)
            print("From:=>",qq)
            print("Subject:=>",ww)
            print("Date:=>",ss)
            print("Content Type :=>",content_type)

G()
file1 = open("MyFile.txt","a")
file2 = open(r"C:\file\MyFile2.txt","w+")
