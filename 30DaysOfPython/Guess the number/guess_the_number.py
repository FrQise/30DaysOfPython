import random

max_range = 100
number = random.randrange(max_range)
number_guess = None
count = 0

while number_guess != number:
    number_guess = input(f"Guess a number between 1 and {max_range} : ")

    try:
        number_guess = int(number_guess)
        if number > number_guess:
            count += 1
            print("The number you need to guess is higher, please enter another number.")
        elif number_guess > number:
            count +=1
            print("The number you need to guess is lower, please enter another number.")
        else:
            print(
                f"Congratulations! You've found the number ! It was : {number} in {count} tries")

    except ValueError:
        print("Please enter a valid number")
        break