# task1:convert same to hierarchical also make use of public,private along with class methods,class variables usage

class RBI:
    'Base Class'
    cash=10000000 #class Variable
    def __init__(self,name,__pin):
        self.name=name  #public
        self.__pin=__pin #private
    def details(self):
        print(f'username:{self.name}')
        print(f'pin:{self.__pin}')
    # get pin
    def get_pin(self):
        return f'pin is {self.__pin}'
    # method
    @classmethod
    def available_cash(cls):
        print(f'Avaiable Cash with RBI is {RBI.cash}')
    


class SBI(RBI):
    "Derived class(1)"
    cash=2500000
    @classmethod
    def sbi_cash(cls):
        print(f'SBI cash is {SBI.cash}')
        print(f'Total cash is {SBI.cash+RBI.cash}')

class HDFC(RBI):
    "Derived class (2)"
    cash=5000000 #class Variable
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {HDFC.cash}')
        print(f'Total cash is {HDFC.cash+RBI.cash}')

class Union(RBI):
    "Derived class(3)"
    cash=4500000
    @classmethod
    def Union_cash(cls):
        print(f'Union cash is {Union.cash}')
        print(f'Total cash is {Union.cash+RBI.cash}')


class Axis(RBI):
    "Derived class (4)"
    cash=5500000
    @classmethod
    def Axis_cash(cls):
        print(f'Axis cash is {Axis.cash}')
        print(f'Total cash is {Axis.cash+RBI.cash}')

print('--- HDFC BANK----')
u1=HDFC('praveen',2340)
u1.details()
print(u1.get_pin())
u1.available_cash()
u1.hdfc_cash()
print("-"*45)

print('--- SBI BANK ---')
u2=SBI('Tony',4590)
u2.details()
print(u2.get_pin())
u2.available_cash()
u2.sbi_cash()
print("-"*45)

print('--- Union Bank ---')
u3=Union('Dhoom',3322)
u3.details()
print(u3.get_pin())
u3.available_cash()
u3.Union_cash()
print("-"*45)

print('--- Axis Bank ---')
u4=Axis('rocky',1951)
u4.details()
print(u4.get_pin())
u4.available_cash()
u4.Axis_cash()