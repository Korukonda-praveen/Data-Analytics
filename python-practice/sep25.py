# anonymous functions--> nameless fucntions (helper function),we define them by using lamba keyword
'''
def area(length,breath):
    a=length*breath
    return a
user_l=float(input('enter the length:'))
user_b=float(input('enter the breath:'))

final_area= area(user_l,user_b)

print(final_area)
'''
# area=lambda side:side**2
# print(area(5))

# fname,lname=input('Enter the names:').split(',')
# full_name=lambda fname,lname:fname.title().strip()+ " "+lname.title().strip()
# print(full_name(fname,lname))

# accepting input from user and find even odd
# n=int(input('Enter a number:'))
# r=lambda n:'even'if n%2==0 else 'odd'
# r1=lambda n: n**2 if n%2==0 else n**3
# print(r(n))
# print('new result is',r1(n))

# names=['codegnan','python','praveen','data','java']
# g=lambda x: x in names
# h=lambda x:  len(x) in names
# o=lambda x: len(x)
# print(g('python'))
# print(h('praveen'))
# print(o('data'))

# filter()--> we want to specific filtered result
# data=[1,3,4,5,24,12,36,3]
# filter only even numbers from list
# new_data=list(filter(lambda x:x%2==0,data))
# print(new_data)
# try above using user defined function.with a for loop

# def final(data):
    # 'filer values'
    # new_data=[]
    # for i in data:
        # if i%2==0:
            # new_data.append(i)
    # return new_data
# print(final(data))

# fliter desired names from the list
# names=['saketh','python','akash','neha','sammer']
# new_names=list(filter(lambda i:len(i)>=6,names))
# print(new_names)

# map()--> it will apply logic for each value (google maps)

# lst=list(map(int,input('Enter the values:').split(',')))
# print(lst)
# data=[1,3,5,7,-23]
# print(data)
# final=set(map(lambda x,y:x+y,lst,data))
# print(final)

# prices=[2000,2500,1500,4500,3000]
# discount of 10% for every price
# dis_price=list(map(lambda price:(price-price*0.1),prices))
# print(dis_price)

# reduce --> functools
# reduce-->it will check for logic and mkae it to a single value

# import functools
# from functools import reduce as r
# result=r(lambda x,y:x*y,[12,3,4,5,6])
# print(result)

# task:try above two cases using functions
'''
data=[1,2,5,4]
def sum(data):
    sum=0
    for i in data:
        sum+=i
    return sum

def mulpty(data):
    mulpty=1
    for j in data:
        mulpty*=j
    return mulpty
print(sum(data))
print(mulpty(data))
'''

# Recursive Function: A Function can call itself
# Factorial,Fibonacci,sum of number....
# Recursive functions -->Baasecase (it teels when to stop the recursion)

n=int(input('Enter the Value:'))
def fact(n):
    'factorial'
    if n==0 or n==1:
        return 1
    elif n<0:
        return n*fact(n-1)
print(fact(n))

# functions are first class objects
# functions can pass another function as argument
# function can return another function
# function can be inside another function
# function can call itself