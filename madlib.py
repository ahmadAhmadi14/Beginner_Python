import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print(f'Sorry, guess again. the number is too low.')
        elif guess > random_number:
            print(f'sorry guess again. the number is too high.')

    print(f'Yay, congratz. You have guessed the number {random_number} Correctly!!!')
guess(10)