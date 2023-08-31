#30 Days of Python
#Day 08

#LEVEL 1

#1 Iterate 0 to 10 using for loop, do the same using while loop.

count_1 = [1,2,3,4,5,6,7,8,9,10]
for numbers in count_1:
    print(numbers)

print("------------------------------------")
count_2 = 0
while count_2 < 10:
    print(count_2)
    count_2 = count_2 + 1

print("------------------------------------")

#2 Iterate 10 to 0 using for loop, do the same using while loop.

count_3 = [1,2,3,4,5,6,7,8,9,10]
for numbers in reversed(count_3):
    print(numbers)

print("------------------------------------")

for numbers in range(10,0,-1):
    print(numbers)

print("------------------------------------")

count_4 = 10
while count_4 > 0:
    print(count_4)
    count_4 = count_4 - 1

print("------------------------------------")

#3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# #
  ##
  ###
  ####
  #####
  ######
  #######

lp_1 = "#"
for i in range(0,8):
    print(lp_1 * i)

print("------------------------------------")

#4 Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for y in range(0,9):
    for x in range(0,9):
        print("#", end="")
    print()

print("------------------------------------")

#5 Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

a = 0
b = 0

while a < 11 and b < 11:
    result = a * b
    print(a, "x", b,"=", result)
    a = a + 1
    b = b + 1

print("------------------------------------")

#6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lst_1 = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in lst_1:
    print(i)

print("------------------------------------")

#7 Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(0,101,2):
    print(i)

print("------------------------------------")

#8 Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(1,101,1):
    if i % 2 != 0:
        print(i)

print("------------------------------------")

#LEVEL 2

#1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.

list_all = list(i for i in range (1,101,1))
print("The sum of all numbers is", sum(list_all))

#2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#sum of all evens
list_a = list(i for i in range(0,101,2))

#sum of all odds

list_b = list(i for i in range (1,101,1))
list_b = list(map(int,list_b))
list_b = list_b[0::2]

print("The sum of all evens is", sum(list_a), "and the sum of all ods is", sum(list_b))

print("------------------------------------")

#LEVEL 3

#1 Loop through the countries and extract all the countries containing the word land.

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

land = [i for i in countries if "land" in i]
print(land)

print("------------------------------------")

#2 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruit = ['banana', 'orange', 'mango', 'lemon']

for i in reversed(fruit):
    print(i)

#3 Go to the data folder and use the countries_data.py file.
