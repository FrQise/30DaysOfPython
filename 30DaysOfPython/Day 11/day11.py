# 30 Days of Python
# Day 11

# LEVEL 1

# 1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(first_number, second_number):
    sum_two_numbers = first_number + second_number
    return sum_two_numbers


print("The sum of 50 + 50 is :")
print(add_two_numbers(50, 50))

print("------------------------------------------")
# 2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.


def area_of_circle(first_r, second_r):
    pi = float(3.14)
    calc_area = pi * first_r * second_r
    return calc_area


print(area_of_circle(5, 5))

print("------------------------------------------")
# 3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback. <= No comprendo


def add_all_nums(*numbers):
    total = 0
    for numberz in numbers:
        total += numberz
    return total


print(add_all_nums(1, 1, 1, 1, 1, 5))

print("------------------------------------------")
# 4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to_fahrenheit.


def convert_celsius_to_fahrenheit(celcius):
    calc_convertion_1 = celcius * 9/5
    convertion_total = calc_convertion_1 + 32
    return convertion_total


print(convert_celsius_to_fahrenheit(10))

print("------------------------------------------")
# 5 Write a function called check_season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.


def check_season(month):
    month = input("Name your month : ").lower()
    if month == "april" or month == "may" or month == "june":
        return "The season is spring"
    elif month == "july" or month == "august" or month == "september":
        return "The season is summer"
    elif month == "october" or month == "november" or month == "december":
        return "The season is autumn"
    elif month == "january" or month == "febuary" or month == "march":
        return "The season is winter"
    else:
        return "This is not a month"

# I could've added month == 01 if user had choosen to input the month number instead of the name but I'm too lazy right now


print(check_season(""))

print("------------------------------------------")
# 6 Write a function called calculate_slope which return the slope of a linear equation

# I still don't know how to calculate a slope and I'm still too lazy to learn it

# 7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

# I'm skipping this question, I don't even know my multiplication table

# 8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.


def print_list(lst_to_print):
    for elements in lst_to_print:
        print(elements)


pizza = ["Margharita", "Diavola", "Marina", "Quattro Stagioni"]
print_list(pizza)

print("------------------------------------------")
# 9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).


def reverse_list(array_to_reverse):
    reversed_array = []
    for elements in range(len(array_to_reverse) - 1, -1, -1,):
        reversed_array.append(array_to_reverse[elements])

    return reversed_array


test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse_list(test_array))

print("------------------------------------------")
# 10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items


def capitalize_list_items(list_to_capitalize):
    capitalized_list = []
    for elements in list_to_capitalize:
        capitalized_elements = elements.capitalize()
        capitalized_list.append(capitalized_elements)

    return capitalized_list


test_list = ["john", "marc", "paul", "edouard"]
print(capitalize_list_items(test_list))

print("------------------------------------------")
# 11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.


def add_item(lst_one, item_to_add):
    lst_one.append(item_to_add)
    return lst_one


test_list_2 = ["It", "Need", "One", "More"]
item_list = "Word"
print(add_item(test_list_2, item_list))

print("------------------------------------------")
# 12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.


def remove_item(lst_two, item_to_remove):
    lst_two.remove(item_to_remove)
    return lst_two


test_list_3 = ["1", "2", "3", "4", "5"]
item_to_delete = "5"
print(remove_item(test_list_3, item_to_delete))

print("------------------------------------------")
# 13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.


def sum_of_numbers(numb_par):
    result = 0
    for nums in range(1, numb_par + 1):
        result += nums
    return result


print(sum_of_numbers(5))

print("------------------------------------------")
# 14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.


def sum_of_odds(numb_par):
    result = 0
    for nums in range(1, numb_par + 1):
        if nums % 2 != 0:
            result += nums
    return result


print(sum_of_odds(10))

print("------------------------------------------")
# 15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.


def sum_of_even(numb_par):
    result = 0
    for nums in range(1, numb_par + 1):
        if nums % 2 == 0:
            result += nums
    return result


print(sum_of_even(10))

print("------------------------------------------")
# LEVEL 2
# 1 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.


def evens_and_odds(pos_int):
    number_of_odds = 0
    number_of_evens = 0

    for nums in range(0, pos_int + 1):
        if nums % 2 == 0:
            number_of_evens += 1
        else:
            number_of_odds += 1

    return f"Number of even digits: {number_of_evens}, Number of odd digits: {number_of_odds}"


print(evens_and_odds(100))

print("------------------------------------------")
# 2 Call your function is_empty, it takes a parameter and it checks if it is empty or not


def is_empty(pars):
    if bool(pars) == True:
        return "Is not empty"
    else:
        return "Is empty"


empty_list = []
print(is_empty(empty_list))
not_empty_list = ["I", "am", "not", "empty"]
print(is_empty(not_empty_list))

print("------------------------------------------")
# 3 Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).


def calculate_mean(mean_list):
    all_data_sum = 0
    number_of_data = 0
    result = 0

    if len(mean_list) == 0:
        return "The list is empty"

    all_data_sum = sum(mean_list)
    number_of_data = len(mean_list)
    result = all_data_sum / number_of_data

    return result


mean_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(calculate_mean(mean_list))

print("------------------------------------------")


def calculate_median(median_list):

    sorted_list = sorted(median_list)
    middle_index = (len(sorted_list)) // 2
    if len(sorted_list) % 2 == 0:
        result = (sorted_list[middle_index - 1] +
                  sorted_list[middle_index]) / 2
    else:
        result = sorted_list[middle_index]
    return result


find_median = [5, 10, 1, 45, 89, 2, 26, 47, 85, 123, 32, 52, 44]
print(calculate_median(find_median))

print("------------------------------------------")


def calculate_mode(mode_list):
    mode_dct = {}
    for items in mode_list:
        if items in mode_dct:
            mode_dct[items] += 1
        else:
            mode_dct[items] = 1
    max_mode = max(mode_dct.values())
    modes = [items for items, count in mode_dct.items() if count == max_mode]

    if len(modes) == 1:
        return modes[0]
    else:
        return modes


find_mode = [5, 5, 5, 5, 10, 25, 64, 25, 5,
             74, 75, 74, 10, 10, 10, 10, 25, 64, 5]
print(calculate_mode(find_mode))

print("------------------------------------------")


def calculate_range(range_list):
    sorted_list = sorted(range_list)
    h = sorted_list[-1]
    l = sorted_list[0]
    result = h - l
    return result


find_range = [5, 10, 33, 2, 4, 8, 55, 49, 85, 64]
print(calculate_range(find_range))

print("------------------------------------------")


def calculate_variance(variance_list):
    mean = calculate_mean(variance_list)
    result = sum((items - mean) ** 2 for items in variance_list) / \
        len(variance_list)
    return result


find_variance = [5, 10, 33, 2, 4, 8, 55, 49, 85, 64]
print(calculate_variance(find_variance))

print("------------------------------------------")


def calculate_std(std_list):
    variance = calculate_variance(std_list)
    result = variance ** 0.5
    return result


find_std = [5, 10, 33, 2, 4, 8, 55, 49, 85, 64]
print(calculate_std(find_std))

print("------------------------------------------")

# LEVEL 3
# Write a function called is_prime, which checks if a number is prime.


def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return f"{number}, is not a prime number"
        else:
            return f"{number}, is a prime number"
    else:
        return f"{number}, is not a prime number"


print(is_prime(7))

print("------------------------------------------")

# Write a functions which checks if all items are unique in the list.


def is_unique(unique_list):
    for items in unique_list:
        if unique_list.count(items) > 1:
            return "There are multiples occurence of the same item in the list"
        else:
            return "This list contains only one occurence of each items"


list_to_check = [1, 2, 4, 5, 7, 8, 9]
print(is_unique(list_to_check))


print("------------------------------------------")

# Write a function which checks if all the items of the list are of the same data type.


def is_same_data(data_list):
    if len(set(type(item) for item in data_list)) > 1:
        return "There are multiples data types in the list"
    else:
        return "This list contains only one data type"

data_type_list = ["test", 1, 2, 3, "retest"]
print(is_same_data(data_type_list))


print("------------------------------------------")

# Write a function which check if provided variable is a valid python variable

def is_valid(var_name):
    keyword_list = ["False","await","else","import","pass","None","break","except","in","raise","True","class","finally","is","return","and","continue","for","lambda","try","as","def","from","nonlocal","while","assert","del","global","not","with","async","elif","if","or","yield"]
    if not (var_name[0].isalpha() or var_name[0] == "_"):
        return f"{var_name} is not a valid variable name"
    for characters in var_name[1:]:
        if not (characters.isalnum() or characters == "_"):
            return f"{var_name} is not a valid variable name"
    if var_name in keyword_list:
        return f"{var_name} is not a valid variable name"
    
    return f"{var_name} is a valid variable name"

test_if_ok = "test_if_ok"
print(is_valid(test_if_ok))

print("------------------------------------------")