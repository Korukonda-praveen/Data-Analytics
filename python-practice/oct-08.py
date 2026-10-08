'''
Polymorphism --> Method Overloading, Method Overriding (super ()), Operator Overloading (usage of magic methods)


# a='5'
# b='6'
# if a and b are intergers-->addition,a and b are strings -->concat
# tenation, if a and b are lists --> Merging
# print(a+b)
# print(6+7)
# print([6,7]+[9,4])
# if u consider imtergers

# a=7;b=8;print(a.__add__(b))

a=[1,2,4]
print(a.__add__([2,3,4])) # a+[2,3,4]
print(a.__len__()) #len(a)
print(a.__delitem__(2)) # del a[2]
print(a)

# now let us understand how above dunder methods such as __add__
# __str__

class WatchHistory:
    "we want to calculate the watch history of user"
    def __init__(self,hours):
        self.hours=hours
    # here if we want to calculate the watch history
a=WatchHistory(120)
b=WatchHistory(40)
# print(a.hours+b.hours) here directly we have taken intergers

class WatchHistory:
    "we want to calculate the watch history of user"
    def __init__(self,hours):
        self.hours=hours
    # here if we want to calculate the watch history
    def __add__(self, value):
        return self.hours + value.hours
a=WatchHistory(120)
b=WatchHistory(40)
print(a+b)
so in above case we are overloading our dudner add method   

class WatchHistory:
    "we want to calculate the watch history of user"
    def __init__(self,hours):
        self.hours=hours
    # here if we want to calculate the watch history
    def __add__(self, value):
        return self.hours + value.hours
    def __str__(self):
        return f'The Watch History is {self.hours}'
a=WatchHistory(120)
b=WatchHistory(40)
# print(a+b)
print(a)
'''
# Abstraction: It is one of the key feature of OOP which helps in implementing important information
#if we want to invoke a specific method from a base class to be applied for all derived classes
# abc module

import abc
from abc import ABC,abstractmethod
# Instagram --> Upload photo,video,reel
class Content(ABC):
    @abstractmethod
    def upload(self):
        pass
class Photo(Content):
    def upload(self):
        print(f'photo is uploading')
    
class Video(Content):
    def upload(self):
     print(f'video is uploading')

    
class reel(Content):
    def upload(self):
        print(f'reel is uploading')

contents=[Photo(),Video(),reel()]
for content in contents:
    content.upload()