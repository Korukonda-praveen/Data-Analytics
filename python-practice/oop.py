'''
OOP--> Object Oriented programming --> It is a principle or paradigm
which revolves around objects,
 
It has two main concepts
--> Attributes (data)-->Characteristics of an object
-->Methods (behaviour)--> It performs the actions for the object

An object is a real world entity,whereas class is a blueprint of an object

chair-->object
tools,wood -->memory
dimensions (blueprint) class
carpenter -->user


Sytax --> class is the keyword

class ClassName:
    "doc string"
    # Attritubtes(Characteristics)
    .............
    ............
    # methods (behaviour)
    def method(self):
        ........
        statement(s)...
        .....
a=Classname()

            (or)
    
            
    class ClassName:
        'doc string'
    def __init__(self,attrs):
     ................
     ............
    def method(self):
        statements.....
        ......


# OOP--> Encapsulation,Inheritance,Polymorphism,Abstraction
# Encapsulation --> It is one of the key properties of OOP,which bundles the data including attributes and methods into a single class
# it also provides accessibility(public,private,protected)


# Students Class with basic details

class Students:
    "Students class with basic details"
    # Attributes
    name='praveen'
    age=20
    location='vizag'

    # Behaviour(actions)
    def details(self):
        print(f'{self.name} is {self.age} years old and is {self.location}')
s1=Students()
# print(dir(s1))
s1.details()
print(s1.__class__) # returns class name (__class__)--> dunder class
print(s1.__doc__) #returns doc string
print(s1.__dict__) # returns empty as we didnot have constructor (method)
# whatever objects we create its only same

s2=Students()
s2.name='jaya'
s2.age=24
s2.location='hyd'
s2.details()


# In the above case we want to modify the attributes such that we can create multiple objects with specific attributed and methods


class Students:
    "students class with actions"
    def profile(self,name,age,email_id,moblie):
        self.name=name
        self.age=age
        self.email=email_id
        self.moblie=moblie
    # To display the details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student email is {self.email} and age is {self.age}')

user=Students()
user.profile('praveen',20,'praveen545792@gmail.com',785942631)
user.display()
print(user.__dict__)





class Students:
    "students class with actions"
    def __init__(self,name,age,email_id,moblie):
        self.name=name
        self.age=age
        self.email=email_id
        self.moblie=moblie
    # To display the details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student email is {self.email} and age is {self.age}')
s1=Students('praveen',20,'praveen545792@gmail.com',123456789)
s1.display()
print(s1.__dict__)
'''
# Task --> create a cars class with attributes as brand,color,price

class Car:
    "create a cars class with attributes as brand,color,price"
    def __init__(self,brand_name,color,price):
        self.name=brand_name
        self.color=color
        self.cost=price
    def display(self):
        print(f'brand name is {self.name}')
        print(f'color of the car is {self.color} and cost of the car is {self.cost}')

c1=Car('BMW','white','2.6cr')
c1.display()
c2=Car('Tata','black','20 lakhs')
c2.display()
        






















