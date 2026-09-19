# Question 1: Student marks file manger

file=open('marks.txt','w')
   
for i in range(1,6):
        user_input=input(f'Enter student mark:')

        try:
            marks=int(user_input)

            if 0<= marks <= 100:
                file.write(f'{marks}\n')
                print('Mark saved successfully')
            else:
                print('Invalid mark')
        except ValueError:
            print('Invalid mark')
file.close()
with open('marks.txt','r')as f:
    print('Saved Marks:')
    for line in f:
        print(line.strip())


# Question 2: Expense Tracker
file=open('expenses.txt','w')

for i in range(1,6):
    try:
        expense=float(input(f'Enter expense {i}: '))

        if expense>0:
            file.write(str(expense)+'\n')
        else:
            print('Expense must be greater than 0.')
    except ValueError:
        print("Invalid expense. Please enter a number.")

file.close()

total=0
try:
    with open('expenses.txt','r')as file:
        print('\nExpenses:')

        for line in file:
            expense=float(line)
            print(expense)
            total+=expense

        print("\nTotal expenses:",total)
except FileNotFoundError:
    print('Expense file not found.')

#Question 3: Student Attendance Manager

file = open('attendance.txt', 'w')

for i in range(1, 6):
    try:
        name = input('Enter student name: ')
        status = input('Enter attendance (P/A): ').upper()

        if status == 'P' or status == 'A':
            file.write(f'{name},{status}\n')
        else:
            print('Invalid attendance status.')

    except Exception:
        print('Invalid input')

file.close()


try:
    with open('attendance.txt', 'r') as f:
        print('\nPresent Students:')

        for record in f:
            name, status = record.strip().split(',')

            if status == 'P':
                print(name)

except FileNotFoundError:
    print('Attendance file not found')

#Question 4: Product Inventory Manager

file = open('inventory.txt', 'a')

for i in range(1, 4):
    try:
        product_name = input('Enter product name: ')
        quantity = int(input('Enter quantity: '))

        if quantity >= 0:
            file.write(f'{product_name},{quantity}\n')
        else:
            print('Quantity cannot be negative')

    except ValueError:
        print('Invalid quantity is entered.')

file.close()


try:
    with open('inventory.txt', 'r') as f:

        print('\nCurrent Inventory:')

        records = f.readlines()

        for record in records:
            product_name, quantity = record.strip().split(',')
            print(f'{product_name} - {quantity}')

        search_name = input('\nEnter product to search: ').strip()
        found = False

        for record in records:
            product_name, quantity = record.strip().split(',')

            if product_name.lower() == search_name.lower():
                print(f'{product_name} is available.\nQuantity: {quantity}')
                found = True

        if found == False:
            print('Product not found')

except FileNotFoundError:
    print('Inventory file not found')

#Question 5: Student Result File Analyzer

passed=0
failed=0
total=0
valid_students=0

try:
    with open('students.txt','r')as f:

        for record in f:
            try:
                name,mark=record.strip().split(',')
                mark=int(mark)

                if mark>=50:
                    result='Pass'
                    passed+=1
                else:
                    result='Fail'
                    failed+=1

                print(f'{name}-{mark}-{result}')

                total+=mark
                valid_students+=1
            except ValueError:
                print(f'Invalid mark for {name}\n')

        avg=total/valid_students     
        print('-'*24)
        print('Result Summary')
        print('-'*24)
        print(f'Passed students:{passed}')
        print(f'Failed students:{failed}')
        print(f'Average mark:{avg}')
except FileNotFoundError:
    print('students.txt file not found')
