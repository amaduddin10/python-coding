import random

def rock_papper_scissor():
    choices=['rock', 'papper', 'scissor']

    while True:
        user_score = 0
        computer_score = 0
        round_number = 1

        print('welcome to rock-papper-scissor-game!')
        print('type ''quit'' anytime to exit.')

        while True:
            print(f'---round{round_number}---')
            print('Avaible choices: rock, papper, scissor, quit')
            user_choice=input('enter your choice ').lower()
            if user_choice=='quit':
                print('thanks for playing!')
                print(f'final scores => you:{user_choice} - computer: {computer_score} ')
                break

            if user_choice not in choices:
                print('invalid input! please enter rock, papper or scissor')
                continue

            computer_choice = random.choice(choices)
            print(f'computer chose{computer_choice}')

            if user_choice==computer_choice:
                print('its a tie!')
            elif(user_choice == 'rock' and computer_choice == 'scissor') or \
                (user_choice == 'scissor' and computer_choice == ' papper') or \
                (user_choice == 'papper' and computer_choice == 'rock'):
                print('you win this round')
                user_score=+ 1
            else:
                print('computer win this round')
                computer_score=+1

            print(f'current scores => you {user_score} ---computer:{computer_score}')
            round_number=+1

            play_again=input('would you like to play again(yes/no)').lower()
            if play_again != 'yes':
                print('goodbye')
                break

rock_papper_scissor()