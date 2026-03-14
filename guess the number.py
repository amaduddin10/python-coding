import random

def guess_the_number():
    print('Welcome to the guees-the-number exeperience')
    print('the number is betwwen 1 and 10.')
    
    total_attempts = 0
    rounds_played = 0

    while True:
        rounds_played += 1 
        target = random.randint(1, 10)
        attempts = 0

        print(f'---round number {rounds_played}---')

        while True:
            user_input=input('enter your guess (1-10):')

            try:
                guess=int(user_input)
            except ValueError:
                print('invalid input. please provide a valid number')
                continue

            if guess < 1 or guess > 10:
                print('please enter a number within the range 1 to 10')
                continue

            attempts += 1
            total_attempts += 1

            if guess < target:
                print('to low. give another guess ')
                continue

            elif guess > target:
                print('to high. give another guess')
                continue
            else:
                print(f'Exelent! you reched the target of {attempts} attemps.')
                break

        replay = input('/n would you like to play another round? (y/n)')

        if replay  != 'y':
            break

    print('/n--- session sumary ---')
    print(f'total round playd{rounds_played}')
    print(f'total attempt {total_attempts}')
    print('thankyou for playing . session terminated')

guess_the_number()