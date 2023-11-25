# 30 Days of Python
# Day 13

#1 Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter = [i for i in numbers if i < 0]
print(filter)

print("------------------------------------------")

#2 Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [number for lst in list_of_lists for sublist in lst for number in sublist]
print(flattened_list)

print("------------------------------------------")

#3 Using list comprehension create the following list of tuples:

lst_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(lst_of_tuples)

print("------------------------------------------")

#4 Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# output: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

countries_flattened = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for tuples in countries for country in tuples]
print(countries_flattened)

print("------------------------------------------")

#5 Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

#output : [{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]

countries_dict = [{"country":country[0].upper(), "city":country[1].upper()} for tuples in countries for country in tuples]
print(countries_dict)

print("------------------------------------------")

#6 Change the following list of lists to a list of concatenated strings:

names = [[('John', 'Doe')], [('David', 'Smith')], [('Spider', 'Man')], [('Oriath', 'BurnToTheGround')]]

names_concatened = [name[0] + " " + name[1] for tuples in names for name in tuples]
print(names_concatened)

print("------------------------------------------")

#7 Write a lambda function which can solve a slope or y-intercept of linear functions.

#Still don't know what a slope is and how to solve/calculate it, so here's a lambda function to calculate the area of a circle

area_of_circle = lambda x: 3.14 * x ** 2
print(area_of_circle(5))