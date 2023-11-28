from functools import reduce
from countries import countries_list
from countries_data_dict import countries_data

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['John', 'Oriath', 'Will', 'BurnToTheGround']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 30 Days of Python
# Day 14

#LEVEL 1
#1 Explain the difference between map, filter, and reduce.

#map() => take a function and an iterable as parameters and apply the function to every item in the iterable
#filter() => take a function and an iterable as paramaters and apply the function to every item in the iterable and return only True (by boolean standard) results
#reduce() => Part of the functools module, it take a function and an iterable as paramaters and return a single value which is the iterable turned into a single accumulated result.

#2 Explain the difference between higher order function, closure and decorator

#higher order function => a function that take another function as a parameter
#closure => a function object that has access to variable in its scope even when the function is called outsided of that scope
#decorator => a function that is called to modify another function with @

#3 Define a call function before map, filter or reduce

numbers = [1,2,3,4,5,6,7,8,9,10]

def divide_by_2(x):
    return x / 2

divided_numbers = map(divide_by_2,numbers)
divided_numbers_list = list(divided_numbers)
print(divided_numbers_list)

def is_odd(x):
    return x % 2 != 0

odd_numbers = filter(is_odd,numbers)
odd_numbers_list = list(odd_numbers)
print(odd_numbers_list)

def add(x,y):
    return x + y

sum = reduce(add, numbers)
print(sum)

print("------------------------------------------")

#4 Use for loop to print each country in the countries list.

for country in countries:
    print (country)

print("------------------------------------------")

#5 Use for to print each name in the names list.

for name in names:
    print(name)

print("------------------------------------------")

#6 Use for to print each number in the numbers list.

for number in numbers:
    print(number)

print("------------------------------------------")

#LEVEL 2
#1 Use map to create a new list by changing each country to uppercase in the countries list

def uppercasing(x):
    return x.upper()

upped_countries = map(uppercasing,countries)
upped_countries_list = list(upped_countries)
print(upped_countries_list)

print("------------------------------------------")

#2 Use map to create a new list by changing each number to its square in the numbers list

def square_numbers(x):
    return x ** 2

squared_numbers = map(square_numbers,numbers)
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)

print("------------------------------------------")

#3 Use map to change each name to uppercase in the names list

upped_names = map(uppercasing, names)
upped_names_list = list(upped_names)
print(upped_names_list)

print("------------------------------------------")

#4 Use filter to filter out countries containing 'land'.

def contain_land(x):
    return "land" not in x.lower()

filtered_land = filter(contain_land, countries)
filtered_land_list = list(filtered_land)
print(filtered_land_list)

print("------------------------------------------")

#5 Use filter to filter out countries having exactly six characters.

def six_char(x):
    return len(x) == 6

six_char_countries = filter(six_char, countries)
six_char_countries_list = list(six_char_countries)
print(six_char_countries_list)

print("------------------------------------------")

#6 Use filter to filter out countries containing six letters and more in the country list.

def more_six_char(x):
    return len(x) >= 6

six_plus_countries = filter(more_six_char, countries)
six_plus_countries_list = list(six_plus_countries)
print(six_plus_countries_list)

print("------------------------------------------")

#7 Use filter to filter out countries starting with an 'E'

def start_with_e(x):
    return x[:1].lower() != "e"

e_countries = filter(start_with_e,countries)
e_countries_list = list(e_countries)
print(e_countries_list)

print("------------------------------------------")

#8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

chained_iterators = map(square_numbers, filter(is_odd, numbers))
chained_iterators_list = list(chained_iterators)
print(chained_iterators_list)

print("------------------------------------------")

#9 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

multiple_data_type = [1,2,3, "quatre", "cinq", "six", 7.0, 8.0]

def get_string_lists(x):
    return isinstance(x, str)

filtered_string = filter(get_string_lists,multiple_data_type)
filtered_string_list = list(filtered_string)
print(filtered_string_list)

print("------------------------------------------")

#10 Use reduce to sum all the numbers in the numbers list.

sum_reduced = reduce(add,numbers)
print(sum_reduced)

print("------------------------------------------")

#11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

def concatenate_countries(accumulator, country):
    return f"{accumulator}, {country}"

concatened_countries = reduce(concatenate_countries,countries)
print(f"{concatened_countries} are north European countries.")

print("------------------------------------------")

#12 Declare a function called categorize_countries that returns a list of countries with some common pattern

def categorize_countries(x):
    return x[:1].lower() == "s"

s_countries = filter(categorize_countries,countries_list)
s_countries_list = list(s_countries)
print(s_countries_list)

print("------------------------------------------")

#13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

def starting_letter(x):
    return x[:1]

countries_start_letter = map(starting_letter,countries_list)

def count_letters():
    counted_letters = {}
    for letters in countries_start_letter:
        if letters in counted_letters:
            counted_letters[letters] += 1
        else:
            counted_letters[letters] = 1
    return counted_letters

print(count_letters())

print("------------------------------------------")

#14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

def get_first_ten_countries():
    return countries_list[:10]

print(get_first_ten_countries())

print("------------------------------------------")

#15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

def get_last_ten_countries():
    return countries_list[-10:]

print(get_last_ten_countries())

print("------------------------------------------")

#LEVEL 3
#Use the countries_data_dict.py file and follow the tasks below:
#1 Sort countries by name, by capital, by population

sorted_countries_by_name = sorted(countries_data, key=lambda country: country['name'])

print(sorted_countries_by_name)

print("------------------------------------------")

sorted_countries_by_capital = sorted(countries_data, key=lambda capital: capital['capital'])

print(sorted_countries_by_capital)

print("------------------------------------------")

sorted_countries_by_population = sorted(countries_data, key=lambda pop: pop['population'], reverse=True)

print(sorted_countries_by_population)

print("------------------------------------------")

#2 Sort out the ten most spoken languages by location.

languages_by_location = []
for country in countries_data:
    languages_by_location.extend(country['languages'])

language_counts = {}
for language in set(languages_by_location):
    language_counts[language] = languages_by_location.count(language)

sorted_languages_by_count = sorted(language_counts.items(), key=lambda lang: lang[1], reverse=True)

top_ten_languages = sorted_languages_by_count[:10]

print(top_ten_languages)

print("------------------------------------------")

#3 Sort out the ten most populated countries.

sorted_countries_by_population_top_ten = sorted(countries_data, key=lambda pop: pop['population'], reverse=True)[:10]

print(sorted_countries_by_population_top_ten)

print("------------------------------------------")