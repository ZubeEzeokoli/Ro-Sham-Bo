import random

def decision(use, co):
    if use.upper() == 'ROCK' and co == 'Paper':
        print('You Lose!')
    elif use.upper() == 'ROCK' and co == 'Scissors':
        print('You win!')
    elif use.upper() == 'PAPER' and co == 'Rock':
        print('You win!')
    elif use.upper() == 'SCISSORS' and co == 'Rock':
        print('You Lose!')
    elif use.upper() == 'SCISSORS' and co == 'Paper':
        print('You win!')
    elif use.upper() == 'PAPER' and co == 'Scissors':
        print('You Lose!')

def tie(use, co):
    if use.upper() == 'ROCK' and co == 'Rock':
        print('Tie!')
    elif use.upper() == 'ROCK' and co == 'Scissors':
        print('Tie!')
    elif use.upper() == 'PAPER' and co == 'Paper':
        print('Tie!')
    
    
print('RO! SHAM! BO!')
user = input()
choice = ['Rock', 'Paper', 'Scissors']
ctr = 0
while user.lower() != 'n':
    if user.lower() == 'rock' or user.lower() == 'paper' or user.lower() == 'scissors' or user.lower() == 'y':
        com = random.choice(choice)
        #if user.upper() == 'PAPER' and com == 'Paper':
            #print('Tie!')
        if user.lower() == 'y':
            user = input('RO! SHAM! BO!\n')
        if user.upper() == com.upper():
            print(com)
            while user.lower() == com.lower():
                tie(user, com)
                print('Choose again')
                user = input()
                com = random.choice(choice)
                print(com)
                ctr += 1
        if user.lower() != com.lower():
            com = random.choice(choice)
            if ctr == 0:
                print(com)
            decision(user, com)
        print('Play again?(y/n)')
        user = input()
    else:
        print('Invalid choice')
        user = input()
