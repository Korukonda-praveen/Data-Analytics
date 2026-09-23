
'''
#Right Angled Trianfle Pattern
for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()


#inverted right angled triangle
for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
    print()

#primid pattern
for i in range(5):
    for j in range(5-i):
        print('',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()

#invereted primid
for i in range(5):
    for j in range(i+1):
        print('',end=' ')
    for k in range(5-i):
        print('*',end=' ')
    print()


#floyd's pattern
num=1
for i in range(4):
    for j in range(i+1):
        print(num,end=' ')
        num+=1
    print()

#floyd's pattern using A,B,C,D
char=65
for i in range(4):
    for j in range(i+1):
        print(chr(char),end=' ')
        char+=1
    print()


#number pattern start from 0

for i in range(5):
    for j in range(i+1):
        print(i,end=' ')
    print()

# start from a,b,c,d
char=65
for i in range(5):
    for j in range(i+1):
        print(chr(char),end=' ')
    char+=1
    print()

#diamond pattern
for i in range(5):
    for j in range(5-i):
        print('',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()

for i in range(4):
    for j in range(i+2):
        print('',end=' ')
    for k in range(4-i):
        print('*',end=' ')
    print()
'''
#functions--> A function is  a block of code that perfroms a sepecific task
# we have a keyword def
#user defined functions,Built-int functions,Anonymous functions,Recursive
'''
Syntax:

def function name(parameters): #function defination
        Doc String(describe your functions)
        statements(s)....
        .....                   # body of the function
        .....
        return value(s)

function name(args) #function call
'''
#positional arguments,keyword arguments,default arguments
#variable length arguments,keyword variable length arguments

#positional arguments--> ord of arguments in function definition and function call should match

#keyword arguments--> name of the arguments should match


def store(item ,price): 
        'keyword arugments usage'
        print(f'item is {item}')
        print(f'price is {price}')
store('milk',36)
print(store(price=45,item='bread'))


#default Aruguments--> we can make any number of arguments as default but we have a thumb rule

#non default arugument follows default arguments


