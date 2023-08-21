#Day 2 : 30 Days of python programming

#Declare multiples variables
first_name = "John"
last_name = "McDonald"
full_name = "John McDonald"
country = "USA"
city = "Dallas"
age = 26
birth_year = 1975
is_married = False
is_true = True
is_light_on = True
favorite_sandwich, favorite_movie, favorite_sauce = "BLT", "Batman", "Dallas"

#Check the type of all the variables

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(birth_year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(favorite_movie))
print(type(favorite_sandwich))
print(type(favorite_sauce))
print("----------------------------------------------------------------------")



#print the length of your first_name
print("My first name have",len(first_name), "letters")
print("My last name have",len(last_name),"letters")

#compare the length of your first_name and last_name
if len(first_name) > len(last_name):
    print("My first name is longer than my last name with", len(first_name), "letters")
else: print("My last name is longer than my first name with", len(last_name), "letters")

#Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

total_sum = num_one + num_two
total_diff = num_one - num_two
total_product = num_one * num_two
total_division = num_one / num_two
total_remainder = num_one % num_two
total_exp = num_one ** num_two
total_floor_division = num_one // num_two

#calculate area of a circle of r=num_one

area_of_circle = 3.14 * pow(num_one, 2)
print(area_of_circle)

#Calculate the circumference of a circle

circum_of_circle = 3.14*(num_one*2)
print(circum_of_circle)

#Take radius as user input and calculate the area.

radius_circle = input("Enter your radius :")
radius_circle_int = int(radius_circle)
client_radius = 3.14 * pow(radius_circle_int,2)
print(client_radius)

#Use the built-in input function to get first name, last name, country and age from a user 
#and store the value to their corresponding variable names

user_first_name = input("Enter your first name : ")
user_last_name = input("Enter your last name : ")
user_country = input("Enter your country : ")
user_age = input("enter your age : ")
print("Your informations are\nname:",user_first_name,"", user_last_name,"\nage:", user_age,"\ncountry:", user_country)