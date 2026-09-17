#exception handling--> It is a mechanism to a program which responds to run time errors or compliations
#exception--> It tries to make our program go in a normal flow
# keywords: try, except, finally 
# for every try except is mandatory..

'''
try:
    code that may cause an error...
except:
    code that handles the error..
finally:
    ----
    ----
#simple scenario to understand the exception
a,b=map(int,input('enter the values:').split(','))
try:
    result=a/b
    print('result=',result)
except Exception as e:
    print(e)


#same above case accept inputs in try block
try:
    a,b=map(int,input('enter the values:').split(','))
    result=a/b
    print('result=',result)
except Exception as e:
    print(e)
'''
# In above case we will get ValueErroe,ZeroDivisonErroe...
#possible types of errors--> TypeError,ValueError,NameError,IndexError,ZeroDivisonError
# AttributeError, Arithmetic Error
'''
try:
    a,b=map(int,input('enter the values:').split(','))
    result=a/b
    print('result=',result)
except ValueError:
    print('only intergers')
except ZeroDivisionError:
    print('make sure the given denominator greater than zero')
except NameError:
    print('check the spellings')
except AttributeError:
    print('check the methods/funtion names properly')
finally:
    print('khatam tata bye bye good bye')


#multiple execeptions at a time
try:
    a=[12,3,4,5]
    print(a[3]) #take one example as print(a[45])
    a.append('codegnan') # take one example as a.apend('codegnan')
    print() # take one example as print(v)
except (IndexError,NameError,AttributeError)as e:
    print(e)
finally:
    print('khatam tata bye bye good bye')
'''
