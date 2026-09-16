'''
input()--> input formatting
print()--> output formatting

a,b=13,4.5
print(a,b)#by default sep=' '
print(a,b,sep=',')
print(9,15,sep=':')
print('codegnan','python','vizag',sep='---->')
#end by default throws new line, we can modify it..
print(a,b,end=' ')
print('codegnan is in vizag',end='\t')
print('pfs6 and da6')


a=int(input('enter a number:'))
b=int(input('enter a number:'))
print('='*20)
print('addition:',a+b)
print('subtract:',a-b)
print('multiply:',a*b)
print('division:',a/b)
print('='*20)


#usage of %d,%f,%s--> prefer this type only when ur working on calculations
#print('usage of %'%(args))

price=45.3;grade='A';stock=15
print('price is %.2f'%price);print('grade is %s'%grade);print('stock is %d'%stock)
'''

#area of circle when radius is 3.5cm,round off the are to 2 decimal values
#take pi value as 3.1416

#radius=3.5;area=3.1416 *(radius**2);print('area of circle is %.2f'%area)

#new style formatting -->fstring(most recommended after python 3.9 version)

#name='codegnan';batch='DA-06';print(f'{batch} is in {name}')

#control block statements-->They control the flow of the program
#conditional statements(if,elif,else)
#repetition statements(loops)(for,while)
#juming statements(break,continue,pass)

#bmi converter (body mass index--> weight,height)
#height--> feets-->1 feet-->12 inches--1 inch-->2.54cm
#1 feet-->30.48cm-->0.
#bmi=weight/((height)**2)
'''
weight=int(input('enter the weight in kgs:'))
height=int(input('enter the height in cm:'))

if weight>0 and height>0:
    bmi=weight/((height/100)**2)
    if bmi<18.5:
        print("underweight")
    elif bmi<=24.9:
        print("normal")
    elif bmi<=29.9:
        print('overweight')
    elif bmi>30:
        print('obesity')
else:
    print('invaild enter')
'''
height=int(input('Enter your choice\n1.ms\n2.cms\n3.feet\n'))

if height==1:
    input_=float(input('enter the height in ms:'))
    height=input_
elif height==2:
    input_=float(input('enter the height in cms:'))
    height=input_/100
elif height==3:
    input_=float(input('enter the  height in feet:'))
    height=input_/3.281
else:
    print('invaild input')

weight=float(input('enter the weight in kgs:'))
if weight>0 and height>0:
    bmi=weight/(height**2)
    if bmi<18.5:
        print("underweight")
    elif bmi<=24.9:
        print("normal")
    elif bmi<=29.9:
        print('overweight')
    elif bmi>30:
        print('obesity')
else:
    print('invaild enter')
