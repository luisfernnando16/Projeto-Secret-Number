import random

computer = random.randint(1, 5)

vidas = 3

while True:

    user = int(input('Choose a number between 1 and 5: '))

    if user == computer:
        print('You chose the right number!')
        print(f'The computer chose the number {computer} and you chose {user}')
        break
    else:
        print('You chose the wrong number!')
        print(f'The computer chose the number {computer} and you chose {user}')
        
    vidas -= 1

    if vidas == 0:
        print('Voce perdeu todas as suas vidas')
        break