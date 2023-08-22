#Day 04 : 30 Days of Python
#Exercises

#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

string_to_concatenate = ('Thirty', 'Days', 'Of', 'Python')
print(" ".join(string_to_concatenate))

#2	Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

string_to_concatenate_2 = ('Coding', 'For', 'All')
print(" ".join(string_to_concatenate_2))

#3  Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4  Print the variable company using print(
print(company)

#5  Print the length of the company string using len() method and print().
print(len(company))

#6  Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7  Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8  Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9  Cut(slice) out the first word of Coding For All string
print(company[0:6])

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))
print(company.index("Coding"))

#11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

#12 Change Python for Everyone to Python for All using the replace method or other methods.
string_to_change = "Python for Everyone"
print(string_to_change.replace("Everyone", "All"))

#13 Split the string 'Coding For All' using space as the separator (split()).
print(company.split(" "))

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string_to_split = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string_to_split.split(","))

#15 What is the character at index 0 in the string Coding For All.
print(company[0])

#16 What is the last index of the string Coding For All.
print(company[-1])

#17 What character is at index 10 in "Coding For All" string.
print(company[10])

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
""" string_to_abbrev = "Python For Everyone"
print(string_to_abbrev[0], string_to_abbrev[7], string_to_abbrev[11]) 

words = "Python For Everyone".split()
print(words[0][0] + words[1][0] + words[2][0])"""

string_to_split = "Python For Everyone"
result = ""
splited_string = string_to_split.split()
for string in splited_string:
    result += string[0]
    
print(result)

#19 Create an acronym or an abbreviation for the name 'Coding For All'.

string_to_split_2 = "Coding For All"
result_2 = ""
splited_string_2 = string_to_split_2.split()
for string_2 in splited_string_2:
    result_2 += string_2[0]
    
print(result_2)

#20 Use index to determine the position of the first occurrence of C in Coding For All.

print("Coding for All".index("C"))

#21 Use index to determine the position of the first occurrence of F in Coding For All.

print("Coding For All".index("F"))

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.

print("Coding For All".rfind("l"))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'

print("You cannot end a sentence with because because because is a conjunction".find("because"))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'

print("You cannot end a sentence with because because because is a conjunction".rfind("because"))

#25 Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'

print("You cannot end a sentence with because because because is a conjunction".replace(" because because because",""))

# 26 Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
 
# 27 Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))

#28 Does ''Coding For All' start with a substring Coding?
print("Coding For All".startswith("Coding"))

#29 Does 'Coding For All' end with a substring coding?
print("Coding For All".endswith("coding"))

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print("    Coding For All      ".lstrip().rstrip())

#31 Which one of the following variables return True when we use the method isidentifier():
#  30DaysOfPython
#  thirty_days_of_python

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

#32 The following list contains the names of some of python libraries: 
#   ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

to_join = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(to_join))

#33 Use the new line escape sequence to separate the following sentences.
#   I am enjoying this challenge.
#   I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

#34 Use a tab escape sequence to write the following lines.
#   Name      Age     Country   City
#   Asabeneh  250     Finland   Helsinki

print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

#35 Use the string formatting method to display the following:
#   radius = 10
#   area = 3.14 * radius ** 2
#   The area of a circle with radius 10 is 314 meters square.
print("Radius = 10\narea = 3.4 * radius **2\nThe Area of a circle with radius 10 is 314 meters square")

radius = "10"
area = "3.14 * radius ** 2"
area_result = 3.14 * 10 ** 2

print("Radius = {}\narea = {}\nThe Area of a circle with radius {} is {} meters square".format(radius, area, radius, area_result))
print("Radius = 10\narea = 3.4 * radius **2\nThe Area of a circle with radius 10 is 314 meters square")

#36 Make the following using string formatting methods:
#   8 + 6 = 14
#   8 - 6 = 2
#   8 * 6 = 48
#   8 / 6 = 1.33
#   8 % 6 = 2
#   8 // 6 = 1
#   8 ** 6 = 262144

num_1 = "8"
num_2 = "6"

print("{} + {} = 14\n{} - {} = 2\n{} * {} = 48\n{} / {} = 1.33\n{} % {} = 2\n{} // {} = 1\n{} ** {} = 262144\n".format(num_1, num_2,num_1, num_2,num_1, num_2,num_1, num_2,num_1, num_2,num_1, num_2,num_1, num_2))

#---------------------------------------------------------------------------------------------------------------