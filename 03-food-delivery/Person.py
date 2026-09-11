# Parent class for Customer and Delivery Partner

class Person:
    def __init__ (self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class Customer(Person):
    def __init__(self, name, phone, email, address):
        Person.__init__(self, name, phone, email)
        self.address = address
        print('Customer created.')

    def __str__(self):
        return 'Name: {}\tPhone: {}\tEmail: {}\tAddress: {}'.format(self.name, self.phone, self.email,self.address)
        
