'''
This is a simple ATM project
Technologies used: basic python:variables,loops operators,data types,functions,module
features: pinchange,deposit,withdraw,check balance,transaction history
security: user authentication using pin
'''
#first we will create a user details dictionary to store the user information



user_details = {
    'name': 'praveen',  
    'adr':'1235645776',
    'pan':'PPP9023P',
    'pin':'2430',
    'balance': 10000   
}
transaction=[]
attmps=3  #Number of attempts allowed
while attmps >0:  # check if the number of attempts is greater than 0
    user_pin = input("Enter your pin: ") 
    if len(user_pin)==4  and  user_pin in user_details['pin']:# check if the pin length is 4 and the pin is correct
        print('welcome to ATM') #if the pin is correct, welcome the user
        choice = input("Enter your choice\n1.Withdraw\n2.Deposit\n3.Check Balance\n4.Change Pin\n5.transaction history \n") #ask the user for their choice
        if choice == '1': 
            withdraw = int(input("Enter the amount to withdraw: "))
            if withdraw <= user_details['balance'] and withdraw%100==0: #check if the withdraw amount is less than or equal to the balance and is a multiple of 100
                user_details['balance'] -= withdraw #it will deduct the withdraw amount from the balance
                transaction.append(f'Withdraw: {withdraw}') #
                print(f'Your new balance is: {user_details['balance']}') #print the new balance
                
            else:
                print('Insufficient balance or this atm can not provide change') #if the withdraw amount is multiple of 100 this message will be printed
            second_choice=int(input("Enter your choice\n1.Home\n2.Exit\n")) 
            if second_choice==1:
                continue
            else:
                break
        elif choice == '2':
            deposit =int(input("Enter the amount to deposit: "))
            if deposit%100==0:
                user_details['balance']+= deposit #it will add the deposit amount to the balance    
                print(f'Your new balance is: {user_details["balance"]}') #print the new balance
                transaction.append(f'deposit: {deposit}')
                
            else:
                print('This atm can not accept change') #if the deposit amount is multiple of 100 this message will be printed
            second_choice=int(input("Enter your choice\n1.Home\n2.Exit\n"))
            if second_choice==1:
                continue
            else:
                break
                
            
        elif choice == '3':
            print(f'Your balance is: {user_details["balance"]}') #print the balance
            second_choice=int(input("Enter your choice\n1.Home\n2.Exit\n"))
            if second_choice==1:
                continue
            else:
                break    

        elif choice == '4': 
            old_pin = input("Enter your old pin: ")
            if old_pin == user_details['pin']:   #check the old pin is correct or not
                new_pin = input("Enter your new pin: ")  #ask the user for the new pin
                user_details['pin'] = new_pin  #it will change the pin to the new pin
                print('Your pin has been changed successfully')  #print the message
                
            else:
                print('Incorrect old pin')  #if the old pin is incorrect, print the message
            second_choice=int(input("Enter your choice\n1.Home\n2.Exit\n"))
            if second_choice==1:
             continue
            else:
                break

        elif choice =='5':
            if len(transaction)==0:
                print('no transactions yet.')
            else:
                for i in transaction[::-1]:
                    print(i)
            second_choice=int(input("Enter your choice\n1.Home\n2.Exit\n"))
            if second_choice==1:
                continue
            else:
                break

    else:
        attmps -= 1  # if the pin is incorrect, decrease the number of attempts
        if attmps>0:  # if the number of attempts is greater than 0, print the number of attempts left
            print(f'Incorrect pin. You have {attmps} attempts left.')
        else:# if the number of attempts is 0, print the message
            print('your card is blocked. Please contact your bank.')  # if the number of attempts is 0, print the message
