## mixin
class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add email logic here

class EmailableContact(Contact, MailSender):
    pass 

class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street 
        self.city = city 
        self.state = state 
        self.code = code 

##### The Diamond Problem 
class Friend(Contact, AddressHolder):
    def __init__(self,
                name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone

## The order in which methods can be called can be adapted on the fly by modifying the __mro__ attribute

class BaseClass:
    num_base_calls = 0 

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1 

class LeftSubclass(BaseClass):
    num_left_calls = 0 

    def call_me(self):
        BaseClass.call_me(self)
        print('Calling method on left Subclass')
        self.num_left_calls += 1 

class RightSubclass(BaseClass):
    num_right_calls = 0 
    
    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print('Calling method on Right Subclass')
        self.num_right_calls += 1 

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0 

    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print('Calling method on Subclass')

##### Use super instead

class BaseClass:
    num_base_calls = 0 

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1 

class LeftSubclass(BaseClass):
    num_left_calls = 0 

    def call_me(self):
        super().call_me()
        print('Calling method on left Subclass')
        self.num_left_calls += 1 

class RightSubclass(BaseClass):
    num_right_calls = 0 
    
    def call_me(self):
        super().call_me()
        print('Calling method on Right Subclass')
        self.num_right_calls += 1 

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0 

    def call_me(self):
        super().call_me()
        print('Calling method on Subclass')

### Use kwargs
### Make sure to include the exact input arguments in the doctring!

class Contact:
    all_contacts = []

    def __init__(self, name = '', email = '', **kwargs):
        super().__init__(**kwargs)
        self.name = name 
        self.email = email 
        self.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street = '', city = '', state = '', code = '', **kwargs):
        super().__init__(**kwargs)
        self.street = street 
        self.city = city 
        self.state = state 
        self.code = code 

class Friend(Contact, AddressHolder):
    def __init__(self, phone= '', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

