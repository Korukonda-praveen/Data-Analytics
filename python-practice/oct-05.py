'''
OOP--> Encapsulation-->It is one of the key properties of OOP,which bundles the data including attributes and methods into a single class
# it also provides accessibility(public,private,protected)

Public Attributes --> These are defined inside the class and can be modified outside the class


class Users:
    'users data'
    def __init__(self,name):
        self.user=name #public attribute
    def details (self):
        print(f'User name is {self.user}')
u1=Users('praveen')
u1.details()
print(u1.user)
u1.user='tony stark'
u1.details()

# Protected Attribute: This is generally preferred in developer point of view
# as a hit, we generally use single underscore before the attribute,they can also be modified outside the class

class Users:
    'users data'
    def __init__(self,name,_otp):
        self.user=name #public attribute
        self._otp=_otp #protected attribute
    def details (self):
        print(f'User name is {self.user}')
u1=Users('praveen',2430)
print(u1._otp)
u1._otp='0560'
print(u1._otp)


# private attribute--> In this case we make the attribute name with double leading underscores,in very specific where
# the attribute need not be accesses directly such as we make it as __var
# python breaches it by name mangling,but we prefer usage of setters and getter accessors/modifiers
class Users:
    'users data'
    def __init__(self,name,_otp,__password):
        self.user=name #public attribute
        self._otp=_otp #protected attribute
        self.__password =__password #private attribute
    def details (self):
        print(f'User name is {self.user}')
u1=Users('praveen',2430,'praveen@2430')
print(u1.user)
print(u1._otp)
# print(u1.__password) it raises attribute error as we ade it private
print(u1._Users__password) # Here NameMangling is used as we can access private attribute by classname with leading underscore usage...

# as NameMangling is not recommended approach we make use of Accessors and Modifiers in python
class Users:
    'users data'
    def __init__(self,name,_otp,__password):
        self.user=name #public attribute
        self._otp=_otp #protected attribute
        self.__password =__password #private attribute
    # To make use of private attributes(getter method)
    def get_password(self):
        # return '*****'
        return self.__password 
    # Now to modify the password (setter method)
    def set_password(self,new_password):
        if len(new_password)>=6:
            self.__password=new_password
            return self.__password
        else:
            return "make sure to have password with min 6 characters"
    def details (self):
        print(f'User name is {self.user}')
u1=Users('praveen',2340,'dark_knight')
print(u1.get_password())
print(u1.set_password('praveen')) #now password is updated for u1 user

print('='*50)
u2=Users('tony stark',3000,'ironman')
print(u2.get_password())
print(u2.set_password('i_am_dhoom'))

# So we prefer usage of Accessors and modifiers in case of private attributes
# to access and modify the data,we can also use it for Protected Attributes...

# Task:use getter and setter methods for both Protected and private 
# attributes (take a new scenario),additionally u can also have


# Inheritance--> Single,Multiple,Multilevel,Hierarchical,Hybrid Inheritance
# It is one of the key features of OOP,which helps in acquiring or reusing the properties (attributes,methods) from one class to another class

class Base_class: #parent class
    statement(s)...
    ........
class Derived_class(Base_class): #child class
    statement(s)......
    .........


# single Inheritance --> Fingerprint


Class A:
    statement(s)....
    ......
Class B(A):
    statement(s).....
    .......
'''
class Users:
    'users details'
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    # initial case we just display
    def full_name(self):
        return self.fname + self.lname
# u1=Users('praveen', 'korukonda')
# print(u1.full_name())
# class User_v1(Users):
    # pass # This is like placeholder (only for syntax)
class User_v2(Users):
    'upating username'
    def update_name(self):
        return self.fname.title().strip()+" "+self.lname.title().strip()
u1=User_v2('praveen', 'korukonda')
print(u1.full_name())
print(u1.update_name())

# using single inheritance we will make use of Class Attribute and Classmetion
# along with the importance of super()(constructor Overriding/method overriding)