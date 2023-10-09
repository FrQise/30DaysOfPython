import random

max_range = 100
number_guess = None
count = 0
guess_the_number = True
answer = None

while guess_the_number == True:
    number = random.randrange(max_range)
    while number_guess != number:
        number_guess = input(f"Guess a number between 1 and {max_range} : ")

        try:
            number_guess = int(number_guess)
            count +=1
            if number > number_guess:
                print("The number you need to guess is higher, please enter another number.")
            elif number_guess > number:
                print("The number you need to guess is lower, please enter another number.")
            else:
                print(f"Congratulations! You've found the number ! It was : {number} in {count} tries")              


        except ValueError:
            print("Please enter a valid number")
            break

    answer = input("Do you want to play again yes / no : ")
    if answer == "no":
        guess_the_number = False
    else: guess_the_number = True