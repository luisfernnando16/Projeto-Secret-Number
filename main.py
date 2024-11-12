import random

user = int(input('Choose a number between 1 and 5: '))
computer = random.randint(1, 5)

if user == computer:
    print('You chose the right number!')
    print(f'The computer chose the number {computer} and you chose {user}')
else:
    print('You chose the wrong number!')
    print(f'The computer chose the number {computer} and you chose {user}')