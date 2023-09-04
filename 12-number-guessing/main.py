import random

def guess_number_generator():
    return random.randrange(1,100)

def check_number_position(guess):
    global guess_number

    return 'Higher' if guess < guess_number else 'Lower'

if __name__ == '__main__':
    guess_number = guess_number_generator()
    print('Welcome to the guessing number gamen')
    live = 0

    print('Select mode (easy or hard)')
    mode = input()

    live = 10 if mode.lower() == 'easy' else 5
    print('live: ', live)

    while True:
        print('Guess the number from 1 to 100')
        guess = int(input())

        if (guess == guess_number or live == 0):
            break

        live -= 1
        print(check_number_position(guess))
        print('Remaining live: {}'.format(live))

    message = 'You win' if guess == guess_number else 'You lose'

    print(message)
