#### The adapter pattern
class AgeCalculator:
    def __init__(self, birthday):
        self.year, self.month, self.day = (
            int(x) for x in birthday.split("-")
        )

    def calculate_age(self, date):
        year, month, day = (int(x) for x in date.split("-"))
        age = year - self.year 
        if (month, day) < (self.month, self.day):
            age -= 1 
        return age 

import datetime 

class DateAgeAdapter:
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)

    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)

class AgeableDate(datetime.date):
    def split(self, char):
        return self.year, self.month, self.day 

#### The facade pattern

### Email server example
import smtplib 
import imaplib

class EmailFacade:
    def __init__(self, host, username, password):
        self.host = host 
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, message):
        if not '@' in self.username:
            from_email = "{}@{}".format(self.username, self.host)
        else:
            from_email = self.username

        message = (
            "From: {0}\r\n" "To: {1}\r\n" "Subject: {2}\r\n\r\n{3}"
        ).format(from_email, to_email, subject, message)

        smtp = smtplib.SMTP(self.host)
        smtp.login(self.username, self.password)
        smtp.sendmail(from_email, [to_email], message)

    def get_inbox(self):
        mailbox = imaplib.IMAP4(self.host)
        mailbox.login(
            bytes(self.username, "utf8"), bytes(self.password, "utf8")
        )  
        mailbox.select()
        x, data = mailbox.search(None, "ALL")
        messages = []
        for num in data[0].split():
            x, message = mailbox.fetch(num, "(RFC822)")
            messages.append(message[0][1])
        return messages

#### The Composite Pattern
class Folder:
    def __init__(self, name):
        self.name = name 
        self.children = {}

    def add_child(self, child):
        pass 

    def move(self, new_path):
        pass 

    def copy(self, new_path):
        pass 

    def delete(self):
        pass 

class File:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def move(self, new_path):
        pass 

    def copy(self, new_path):
        pass 

    def delete(self):
        pass 

#Extract some of the common methods into a parent class
def get_path(path):
    names = path.split("/")[1:]
    node = root 
    for name in names:
        node = node.children[name]
    return node 

class Component:
    def __init__(self, name):
        self.name = name

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self 
        self.parent = new_folder

    def delete(self):
        del self.parent.children[self.name]

class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_child(self, child):
        child.parent = self 
        self.children[child.name] = child 

    def copy(self, new_path):
        pass 

class File(Component):
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents

    def copy(self, new_path):
        pass 

root = Folder("")




