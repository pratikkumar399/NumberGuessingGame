import random

# user guesses the number
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print("Plzz guess a higher number")
        elif guess > random_number:
            print("Plzz guess a lower number ")

    print(
        f"Congrats you guessed the correct number . {random_number} is the Secret number")


guess(200)

# computer guesses the number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} to high(H), to low (L), or correct(c) ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'{guess} is the correct number ')


computer_guess(200)


