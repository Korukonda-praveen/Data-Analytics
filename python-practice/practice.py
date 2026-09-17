
try:
    marks=int(input('enter your marks:'))
    if marks<0 or marks>100:
        print('Invalid marks entered')
    elif marks>=90:
            print('Grade:A')
            print('Remark:Outstanding!')
    elif marks>=80 and marks<=89:
            print('Grade:B')
            print('Remark:Excellent!')
    elif marks>=70 and marks<=79:
            print('Grade:C')
            print('Remark:Good')
    elif marks>=60 and marks<=69:
            print('Grade:D')
            print('Remark:Fair,needs improvement')
    elif marks>=50 and marks<=59:
            print('Grade:E')
            print('Remark:Poor,needs serious improvement')
    else:
        print('Grade:F')
        print('Remark:Failed,needs to reappear')
except ValueError:
    print('enter only marks')


   
try:
    num=int(input('enter a number:'))

    if num==0:
        print("Zero is neither even nor odd")
    elif num<0:
        if num % 2 == 0:
            print("Negative Even Number")
        else:
            print("Negative Odd Number")
    else:
        if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")
except ValueError:
    print('enter only numbers')

try:
    month=int(input('enter the month number:'))

    if (month==12 or month==1 or month==2):
        print('Season: Winter')
    elif (month==3 or month==4 or month==5):
        print('Season: Spring')
    elif (month==6 or month==7 or month==8):
        print('Season: Summer')
    elif (month==9 or month==10 or month==11):
        print('Season: Autumn')
    else:
        print('Invalid month entered ')
except ValueError:
    print('enter only months between 1 to 12')

