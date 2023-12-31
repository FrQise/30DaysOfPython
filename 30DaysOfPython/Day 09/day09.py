# 30 Days of Python
# Day 09

# LEVEL 1

# 1  Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
#   If below 18 give feedback to wait for the missing amount of years.


usr_age = int(input("Enter your age : "))

if usr_age >= 18:
    print("You are old enough to drive")
elif usr_age == 17:
    print("You need one more year to drive")
else:
    print("You need", 18 - usr_age, "more years to drive")


# 2  Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
#   You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

your_age = int(input("Enter your age : "))
my_age = 28

if your_age == my_age:
    print("We have the same age !")
    if your_age == 27:
        print("You're one year younger than me")
    if your_age == 29:
        print("You're one year older than me")
elif your_age > my_age:
    print("You're", your_age - my_age, "years older than me")
else:
    print("You're", my_age - your_age, "years younger than me")

# 3  Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

nmbr_01 = int(input("Enter one number : "))
nmbr_02 = int(input("Enter a second number : "))

if nmbr_01 > nmbr_02:
    print(nmbr_01, "is greater than", nmbr_02)
elif nmbr_01 < nmbr_02:
    print(nmbr_01, "is smaller than", nmbr_02)
else:
    print(nmbr_01, "is equal to", nmbr_02)


# LEVEL 2

# 1  Write a code which gives grade to students according to theirs scores:
#   90-100, A
#   70-89, B
#   60-69, C
#   50-59, D
#   0-49, F

score = int(input("Enter your score : "))

if score >= 90:
    print("Your grade is A")
elif score >= 70:
    print("Your grade is B")
elif score >= 60:
    print("Your grade is C")
elif score >= 50:
    print("Your grade is D")
else:
    print("Your grade is F")

# 2  Check if the season is Autumn, Winter, Spring or Summer.
#   If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter.
#   March, April or May, the season is Spring June, July or August, the season is Summer

months = (("december", "january", "febuary"), ("march", "april", "may"),
          ("june", "july", "august"), ("september", "october", "november"))
usr_months = (input("Enter your months : "))
if usr_months.lower() in months[0]:
    print("The season is Winter")
elif usr_months.lower() in months[1]:
    print("The season is Spring")
elif usr_months.lower() in months[2]:
    print("The season is Summer")
elif usr_months.lower() in months[3]:
    print("The season is Autumn")
else:
    print("This is not a season")

# 3 The following list contains some fruits:
#  fruits = ['banana', 'orange', 'mango', 'lemon']
#  If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']

your_fruit = input("Input your fruit : ")

if your_fruit.lower() in fruits:
    print("That fruit already exist in the list !")
else:
    fruits.append(your_fruit), print(fruits)

# LEVEL 3

# 4 Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB,
#   print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
#   else print('unknown title') - for more accurate results more conditions can be nested!
# * If the person is married and if he lives in Finland, print the information in the following format:
#   Asabeneh Yetayeh lives in Finland. He is married.


if "skills" in person:
    print(person["skills"][len(person['skills'])//2])
    if "Python" in person["skills"]:
        print("Python" in person["skills"])

print("------------------------------------------")

if "Javascript" or "React" in person["skills"]:
    if "Node" or "Python" or "MongoDB" in person["skills"]:
        print("He is a fullstack developer")
    else:
        print("He is a front end developer")
elif "Node" or "Python" or "MongoDB" in person["skills"]:
    print("He is a back end developer")
else:
    print("Unknown title")

print("------------------------------------------")

if "Finland" in person["country"] and person["is_married"] == True:
    print(person["first_name"], person["last_name"],
          "lives in", person["country"], ". He is married.")
