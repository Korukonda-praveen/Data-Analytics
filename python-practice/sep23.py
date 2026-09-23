# Variable length aruguments (*args),keywrod variable length arugments(**kwargs)
#variable length aruguments: We can pass any number of arguments,but the data will be stored in a________,
# but we use symbolically *args as representation
'''
def new(*a):
    'Usage of Variable length aruguments'
    print(a)
    print(type(a))
new(1,2,3)
new('praveen','python')

print('-'*20)

details=[1234,'data','webinar','hackathon']
new(details)
new(*details)


a,b,c=1,3,4
a,*b,c=1,'praveen','data','codegnan',20
print(a);print(b);print(c)

# * is mainly used to unpack the values from a collection
# a=['codegnan','python','data',45,6.7]
# print(*a)
# for i in a:
    # print(i,end=' ')
# in above case both for loop and line 25 result is same 

#find the sum of arguments in a function

def add(*a):
    'sum of arguments usage using *args'
    print(a)
    print(type(a))
    # we need to have output variable
    result=0
    for i in a:
        if isinstance(i,(int,float )):
            # if type(i)==int or type(i)==float
            # if type(i)in (int,float)
            # except typeerror:
            result=result+i
            # countiue
    return result
print(add(12,3,4,'codegnan','praveen',2.3))

# Keyword variable length arguments--> we can pass any number of keyword arguments ,
#we will use the representation as **kwargs,data is stored in dictionary...


def admission(**kwargs):
    'usage of keyword variable length arguments'
    print(kwargs)
    print(type(kwargs))
# admission() 
admission(name='praveen',phno=8142061224,email_id='praveen545792@gmail.com')



details={'idno':[234,345,342],
         'names':['akash','dileep','sunny'],
         'batches':['da','pfs','jfs']}
admission(**details)


# usage of both *args and **kwargs into a function

def simple(*a,**b):
    'usage of *args and **kwargs'
    print(a)
    print(b)
    result=0
    for i in a:
        if type(i)in (int,float):
             result=result+i
    print(result)
    for key,value in b.items():
        print(f'Key is {key}')
        print(f'Value is {value}')
simple(1,2,3,'poll',23,name='codegnan',place='vizag')
# simple(23,4,batch='pfs06',data='python',3.5)
# positional arguments always follow keyword arguments
'''