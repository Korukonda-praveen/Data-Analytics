import random
player1=input('Enter any one the below:\n1.Rock\n2.Paper\n3.Scissors\n').lower()
player2=random.choice(['Rock','Paper','Scissors']).lower()
print(player2)

if player1=='rock' and player2 =='paper':
    print('player2 won')
elif player1=='paper' and player2 =='scissors':
    print('player2 won')
elif player1=='scissors' and player2 =='rock':
    print('player2 won')
elif player1== player2:
    print('its a tie')
else:
    print('player1 won')