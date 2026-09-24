# scope of the variables --> Scope is basically the region or area where the data is accessible 
# Local scope, Global scope,Global keyword, enclosing scope (non local keyword) Built-in scope
# Local scope (local variables)--> Variable(s) defined inside the function are accessible only

# def data():
    # 'local scope'
    # name='codegnan'
    # return f'{name} is in vizag.'
# print(data())
# print(name) raises NameError
# global scope --> variable defined outside the function can accessible  inside the function
'''
count=10 #global variable
def details():
    'Global scope'
    count=15  #local variable
    print(f'value of count is {count} inside the function')
    count =count+5 
details()
print(f'value of count is {count} inside the function')

count=10 #global variable
def details():
    'usage of global variable'
    global count
    count +=15 
    print(f'value of count is {count} inside the function')   
details()
print(f'value of count is {count} outside the function')

# Enclosing scope-->nested function

def outer():
    'neste functions'
    count=5
    def inner():
        'inner function to use count variable'
        # print(count)
        nonlocal count
        count*=4
        print(f'value of count is {count} inside')
    inner()
    print(f'value of count is {count} outside')
outer()
'''
#import this
# Build-in Scope->Usage of built-in functions as variable

# print(dir(__builtins__))

# print(float(int(bool(24)))) functions as first class objects
# print(abs(-42)) returns the absolute value
# x=[23,45,35]
# x.append(None)
# print(all(x)) # all(iterable)it needs all values in the iterable to be exist

# print(bin(1)) return the binary values
# print(chr(60)) return the concerned object(char)
# print(ord('p')) retun the ASCII value for any character,symbol
# print(round(5.345)) didgits to be rounded off
# print(pow(4,2)) #base,exponent
# print(divmod(6,2)) #perfom 6//2 (quotient)-->6%2
