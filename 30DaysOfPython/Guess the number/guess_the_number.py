import random

number = random.randrange(100)
number_guess = None

while number_guess != number:
    number_guess = input("Guess a number between 1 and 100 : ")
    number_guess = int(number_guess)

    if number > number_guess:
        print("The number you need to guess is higher, please enter another number.")
    elif number_guess > number:
        print("The number you need to guess is lower, please enter another number.")
    else:
        print(f"Congratulations! You've found the number ! It was : {number}")
        break