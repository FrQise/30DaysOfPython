#30 Days of Python
#Day 05

#1  Declare an empty list

empty_list = list()

#2 Declare a list with more than 5 items

list_five_items = ["One","Two","Three","1","2","3"]

#3 Find the length of your list

print(len(list_five_items)) 

#4 Get the first item, the middle item and the last item of the list

item_1_3_5 = list_five_items[0], list_five_items[len(list_five_items) // 2], list_five_items[-1]
print(item_1_3_5)

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["John Doe", "150", "1m05", "Married to the street", "742 evergreen terrace"]

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7 Print the list using print()

print(it_companies)

#8 Print the number of companies in the list

print("There is", len(it_companies), "companies in the list")

#9 Print the first, middle and last company

companies_1_mid_last = it_companies[0], it_companies[len(list_five_items) // 2], it_companies[-1]
print(companies_1_mid_last)

#10 Print the list after modifying one of the companies

it_companies[-1] = "Spotify"
print(it_companies)

#11 Add an IT company to it_companies

it_companies.append("Amazon")
print(it_companies)

#12 Insert an IT company in the middle of the companies list

it_companies.insert(4, "Twitter")
print(it_companies)

#13 Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[-1] = it_companies[-1].upper()
print(it_companies)

#14 Join the it_companies with a string '#;  '

it_companies_join = '#'.join(it_companies)
print(it_companies_join)

#15 Check if a certain company exists in the it_companies list.

does_twitter_exist = "Twitter" in it_companies
print(does_twitter_exist)

#16 Sort the list using sort() method

it_companies.sort()
print(it_companies)

#17 Reverse the list in descending order using reverse() method

it_companies.reverse()
print(it_companies)

#18 Slice out the first 3 companies from the list

print(it_companies[0:3])

#19 Slice out the last 3 companies from the list

print(it_companies[-3:])

#20 Slice out the middle IT company or companies from the list

print(it_companies[len(it_companies) // 2])

#21 Remove the first IT company from the list

del(it_companies[0])
print(it_companies)

#22 Remove the middle IT company or companies from the list

del(it_companies[len(it_companies) // 2])
print(it_companies)

#23 Remove the last IT company from the list

del(it_companies[-1])
print(it_companies)

#24 Remove all IT companies from the list

del(it_companies[0:])
print(it_companies)

#25 Destroy the IT companies list

del it_companies

#26 Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

all_end = front_end + back_end
print(all_end)

#27 After joining the lists in question 26.
# Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack = all_end.copy()

full_stack.extend(["Python", "SQL"])
print(full_stack)

#LEVEL2
#1 The following is a list of 10 students ages:
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age

ages.sort()
print(ages)
print(min(ages))
print(max(ages))

#Add the min age and the max age again to the list

ages.append(ages[1])
ages.append(ages[-1])
print(ages)

#Find the median age (one middle item or two middle items divided by two)
median_age = ages[len(ages) // 2]
print(median_age)

#Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print(average_age)

#Find the range of the ages (max minus min)

print(max(ages) - min(ages))

#Compare the value of (min - average) and (max - average), use abs() method

average_min = abs(min(ages) - average_age)
average_max = abs(max(ages) - average_age)
print(average_min,average_max)
print(average_min == average_max)

#Find the middle country(ies) in the countries list :
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
#Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[0:len(countries)//2+1]
second_half = countries[len(countries)//2+1:]
print(len(countries))
print(len(first_half))
print(len(second_half))

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.

countries_to_unpack = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
non_scandic = countries_to_unpack[0:3]
scandic = countries_to_unpack[3:]
print(non_scandic)
print(scandic)