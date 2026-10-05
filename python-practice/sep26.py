# Funtions --> user defined functions,built in functions,anonymous functions (lambda keyword),recursive functions--> procedure oriented programming

# modules --> A python file containing variables, functions and classes,objects
# userdefined modules(import),built-in Moules,available modules (pypi)

def details(name,place):
    'details to be stored'
    print(f'Name is {name}')
    print(f'Place is {place}')
# details('praveen','vizag')


data={'ids':[12,34,43,23],
      'names':['praveen','jayakumar','usha sri'],
      'batches':['da-06','pfs-06','jfs-06']}



# if __name__ == '__main__': #we call __name__ as dunder name
    # details('praveen','vizag')
    # print(data)

print(__name__)