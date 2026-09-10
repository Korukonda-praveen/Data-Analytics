'''
marks=[]
for mark in range(3):
    mark=int(input('Enter the marks:'))
    marks.append(mark)
marks.insert(0,90)
marks.extend([75,85])
if 75 in marks:
    marks.remove(75)
print(marks.pop())
print(marks)
print('final list is',marks)
print('length of the list is',len(marks))





numbers=[20,10,30,20,40,20]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

num=int(input('enter a number:'))

if num in numbers:
   print("count is", numbers.count(num))
   print('index is', numbers.index(num))
else:
   print('no found')
                               
numbers=[10,15,20,25,30,35]
even=[]
odd=[]

for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

f=numbers.copy()
print(f)
numbers.clear()
print(numbers)
'''