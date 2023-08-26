#30 Days of Python
#Day 06

#LEVEL 1

#1 Create an empty tuple

empty_tuple = tuple()

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

familly_sisters = ("Lisa", "Maggie")
familly_brothers = ("Bart", "Hugo")
print(familly_brothers)
print(familly_sisters)

#3 Join brothers and sisters tuples and assign it to siblings

siblings = familly_sisters + familly_brothers
print(siblings)

#4 How many siblings do you have?
print("I have", len(siblings), "siblings")

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = list(siblings)
print(family_members)
family_members.extend(("Marge", "Homer"))
family_members = tuple(family_members)
print(family_members)
print(type(family_members))

#LEVEL 2

#1 Unpack siblings and parents from family_members

siblings_unpack = family_members[0:4]
print(siblings_unpack)
parents_unpack = familly_sisters[4:]
print(parents_unpack)

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("Banana", "Orange", "Apples")
vegetables = ("Potatoes", "Onions", "Lettuce")
animal_product = ("Beef", "Pork", "Cheese")

food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(type(food_stuff_lt))

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

print(food_stuff_tp[len(food_stuff_tp)//2])

#5 Slice out the first three items and the last three items from food_staff_lt list

print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

#6 Delete the food_staff_tp tuple completely

del(food_stuff_tp)

#7 Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)

