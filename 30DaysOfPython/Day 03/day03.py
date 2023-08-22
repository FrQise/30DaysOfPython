#Day 03 : 30 Days of Python
#Exercises

#1
my_age = 28

#2
my_height = 1.75

#3
number_complex = 1+1j

#4
""" print("The area of the triangle is :", 0.5 * int(input("Base : ")) * int(input("Height : ")))

triangle_base = int(input("Enter the base of the triangle : "))
triangle_height = int(input("Enter the height of the triangle : "))
print("The area of the triangle is : ", 0.5 * triangle_base * triangle_height) """

#5

""" print("The area of the triangle is : ", int(input("Side a : ")) + int(input("Side b : ")) + int(input("Side c : "))) """

#6

""" rectangle_width = int(input("Enter the width of your rectangle : "))
rectangle_length = int(input("Enter the length of your rectangle : "))
print("The area of your rectangle is : ", rectangle_length * rectangle_width)
print("The perimeter of your rectangle is : ", 2 * (rectangle_width + rectangle_length)) """

#7

""" triangle_radius = int(input("Enter the radius of your circle : "))
print("The area of your circle is : ", 3.14 * triangle_radius * triangle_radius)
print("The circumference of your circle is : ", 2 * 3.14 * triangle_radius) """

#8, 9 10
print("I don't know how to calculate a slope & I am too lazy to learn right now")

#11
print("I don't know a damn thing about maths")

#12

print("This is the length of Dragon :" , len("Dragon"),"and this is the length of Python :", len("Python"))
print("Is Python lengthier than Dragon ?", len('python') > len('dragon'))

#13

print("Is the letters 'on' in the word Python and in the word Dragon ?", 'on' in 'python' and 'on' in 'dragon')

#14

print("Is 'jargon' in the sentence : ", "jargon" in "I hope this course is not full of jargon")

#15

print('on' not in 'python' and 'on' in 'dragon')

#16

length_python = float(len("Python"))
print(type(length_python))
length_python_string = str(length_python)
print(type(length_python_string))

#17

""" check_if_even = int(input("Enter your number : "))
if check_if_even % 2 == 0:
    print("Even")
else: print("Odd") """

#18

print(7//3 == 2.7)

floor_division = 7 // 3
if floor_division == 2.7:
    print("Is equal to 2.7")
else: print("Is not equal to 2.7")

#19
print("Is type('10') equal to type(10) : " , type("10") == type(10))

#20

print("Is int(9.8) equal to 10 : ", int(9.8) == 10)

#21

number_of_hours = int(input("Enter your numbers of hours : "))
rate_per_hours = int(input("Enter your rate per hours : "))
print("Your weekly earning is : ", number_of_hours * rate_per_hours)

#22

years_lived = int(input("Enter the years you have lived : "))
print(years_lived * 365 * 24 * 60 * 60 * 60)

#23

for table in range(1, 6):
    print(table, table ** 0, table ** 1, table ** 2, table ** 3)