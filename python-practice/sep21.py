'''
Nested loops -->(for in for) --> These are primarily used for pattern printings
Matrix operations and problems solving scenarios (data structures)....

for <temp> in range(obj):
        statement(s)..

        
syntax:
for i in range(outer_loop_range):
    for j in range(inne_loop_range): #inner loop will be completely executed for every outer loop
    #code block
    for i in range(3): #i--> 0,1,2
    for j in range(2): #j--> 0,1
        print(f'i={i}, j={j}')
#In above case for complete j value of 0 i value will be 0,1,2 and follows same for others

for i in range(3): # In this case  both i and j are same
    for j in range(3):
        print(i,j)

for i in range(3): 
    for j in range(3):
        print( i,j,end=' ') # now entrie result will be  in one single line
        print('python')
    print('='*20) #only when inner loop is complete before starting outer loop it generates
    
for i in range(2): #i->0,1
    for j in range(i+1): # first i value will be 0 loop doesn't start for j
        print(f'i={i},j={j}')

print('-'*20)
for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()

for i in range(3):
    for j in range(4):
        print(  j+1,end=' ')
    print()


for i in range(4):
    for j in range(4):
        print(i+1,end=' ')
    print()
    num=1
for i in range(3):
    for j in range(3):
        print(num, end=' ')
        num+=1
    print()

char=65
for i in range(4):
    for j in range(4):
        print(chr(char),end=' ')
    char+=1
    print()

print('-'*20)

char=65
for i in range(4):
    for j in range(4):
        print(chr(65+j),end=' ')
    print()
'''

num=tuple(map(int, input().split()))

even=()
odd=()

for i in num:
    if i%2==0:
        even+=(i,)
    else:
        odd+=(i,)

print("even numbers:",*even)
print("odd numbers:",*odd)