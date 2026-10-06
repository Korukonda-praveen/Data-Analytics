'''
# Banking Scenario --> single Inheritance

class RBI:
    'Base Class'
    cash=10000000 #class Variable
    # class method
    @classmethod
    def available_cash(cls):
        print(f'Avaiable Cash with RBI is {RBI.cash}')
# u1=RBI()
# print(RBI.cash)
# u1.available_cash()
# RBI.available_cash()

class SBI(RBI):
    "Derived class"
    pass
# u2=SBI()
# print(SBI.cash)
# u2.available_cash()

class HDFC(RBI):
    "Derived class 2"
    cash=5000000 #class Variable
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        print(f'Total cash is {cls.cash+RBI.cash}')
u3=HDFC()
print(u3.cash)
u3.available_cash()
u3.hdfc_cash()

# task1:convert same to hierarchical also make use of public,private along with class methods,class variables usage

# kid-fater property scenario--> constructor overriding,method overriding

class Father:
    'Father Property only interms in cash'
    def __init__(self):
        self.property=5000000
    def father_prop(self):
        print(f'Father Property is {self.property}')
# class kid(Father):
    # pass
class kid(Father):
    "kid has started earning"
    def __init__(self):
        self.property=250000
    def kid_prop(self):
        print(f'Kid property is {self.property}')
        print(f'Total Property is {self.property + self.property}')
# obj=Father()
# obj.father_prop()
obj=kid()
obj.father_prop()
obj.kid_prop()


# In Above we have seen contructor Overriding, as we defined constructors in the base class
# base class and derived class(child class),child class 

# constructor overrifing can be avoided by usage of super()
# calling superclass constructor --> super().__init__()
# calling superclass constructor with args--> super().__init__(args)
# calling superclas method --> super().method()
class Father:
    'Father Property only interms in cash'
    def __init__(self):
        self.fproperty=5000000
    def father_prop(self):
        print(f'Father Property is {self.fproperty}')
# class kid(Father):
    # pass
class kid(Father):
    "kid has started earning"
    def __init__(self):
        super().__init__() #calling superclass constructor
        self.kproperty=250000
    def kid_prop(self):
        print(f'Kid property is {self.kproperty}')
        print(f'Total Property is {self.kproperty + self.fproperty}')
# obj=Father()
# obj.father_prop()
obj=kid()
obj.father_prop()
obj.kid_prop()

class Father:
    'Father Property only interms in cash'
    def __init__(self,prop1):
        self.fproperty=prop1
    def father_prop(self):
        print(f'Father Property is {self.fproperty}')
# class kid(Father):
    # pass
class kid(Father):
    "kid has started earning"
    def __init__(self,prop2,prop1):
        super().__init__(prop1) #calling superclass constructor with args
        self.kproperty=prop2
    def kid_prop(self):
        print(f'Kid property is {self.kproperty}')
        print(f'Total Property is {self.kproperty + self.fproperty}')

obj=kid(450000,2500000)
obj.father_prop()
obj.kid_prop()
'''
# method overriding --> when we define same method same in parent class and also in child class
# it will result in method overriding ,to get rid of this we prefer --> super().method()

class Square:
    "Base class"
    def __init__(self,x):
        self.x=x
    def area(self):
        print( f'Area of Square {self.x**2}')
class Rectangle(Square):
    "Derived class with constructor and method name same"
    def __init__(self,y,x):
        super().__init__(x)
        self.y=y
    def area(self):
        super().area()
        print(f'Area of Rectangle {self.x*self.y}')
x,y=map(int,input('Enter the values:').split(','))
obj=Rectangle(x,y)
obj.area()

# Method overriding will only happen with Inheritance usage

# Task 2 real time scenario for Multiple Inheritance
# Multiple Inheritance:one derived class with more than one bas classes
# parent (father,mother)--->child

'''
class A:
    statement(s)...
    ......
class B:
    statement(s)...
    ......
class c(a,b):
    statements(s)....
    ......

'''