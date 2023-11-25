import random
# 30 Days of Python
# Day 12

# LEVEL 1

# 1 Write a function which generates a six digit/character random_user_id.

def random_user_id():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_user_id = "".join(random.choice(characters) for n in range(6))
    return random_user_id

print(random_user_id())

print("------------------------------------------")

# 2 Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user():
    number_of_char = int(input("Please enter the number of character you want your ID to contains : "))

    number_of_id = int(input("Please enter the number of ID you need to generate :"))
    
    generated_ids = []
    for n in range(number_of_id):
        generated_ids.append(generate_user_id(number_of_char))
    return generated_ids

def generate_user_id(number_of_char):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    user_id = "".join(random.choice(characters) for n in range(number_of_char))
    return user_id

print(user_id_gen_by_user())

print("------------------------------------------")

# 3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# rgb(125,244,255) - the output should be in this form

def rgb_color_gen():
    gen1 = random.randint(0, 255)
    gen2 = random.randint(0, 255)
    gen3 = random.randint(0, 255)
    rgb = f"rgb({gen1}, {gen2}, {gen3})"
    return rgb

print(rgb_color_gen())

print("------------------------------------------")

# LEVEL 2
# 1 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f

def list_of_hexa_colors(number_of_hexa):
    characters = "abcdef0123456789"
    generated_hexa = ["".join(random.choice(characters) for n in range (6)) for x in range(number_of_hexa)]
    return generated_hexa
print(list_of_hexa_colors(5))

print("------------------------------------------")

# 2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def rgb_color_array(number_of_rgb):
    gen1 = random.randint(0, 255)
    gen2 = random.randint(0, 255)
    gen3 = random.randint(0, 255)
    rgb_color_gen = f"rgb{gen1}, {gen2}, {gen3}"
    generated_rgb = [rgb_color_gen for n in range (number_of_rgb)]
    return generated_rgb
print(rgb_color_array(3))

print("------------------------------------------")

#3 Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(color_type, number_of_colors):
    if color_type == "hexa":
        return list_of_hexa_colors(number_of_colors)
    elif color_type == "rgb":
        return rgb_color_array(number_of_colors)
    else:
        return []
    
print(generate_colors("rgb",3))

# LEVEL 3
# 1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(input_list):
    random.shuffle(input_list)
    return input_list
list_to_shuffle = [1,2,3,4,5,6,7,8,9,10,11,12]
print(shuffle_list(list_to_shuffle))

# 2 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def generate_unique_numbers():
    unique_numbers = set()

    while len(unique_numbers) < 7:
        unique_numbers.add(random.randint(0,9))
    return list(unique_numbers)

print(generate_unique_numbers())