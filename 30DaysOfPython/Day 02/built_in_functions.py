            #-------------------------------------------------------------------------------------------
            # ______        _ _         _____          _______                      _                    
            #(____  \      (_) |_      (_____)        (_______)                _   (_)                   
            # ____)  )_   _ _| | |_       _   ____     _____ _   _ ____   ____| |_  _  ___  ____   ___   
            #|  __  (| | | | | |  _)     | | |  _ \   |  ___) | | |  _ \ / ___)  _)| |/ _ \|  _ \ /___)  
            #| |__)  ) |_| | | | |__    _| |_| | | |  | |   | |_| | | | ( (___| |__| | |_| | | | |___ |  
            #|______/ \____|_|_|\___)  (_____)_| |_|  |_|    \____|_| |_|\____)\___)_|\___/|_| |_(___/ 
            #-------------------------------------------------------------------------------------------
            #                       Training on Python3 Built In Functions
            #                                    FrQise - 2023
            #-------------------------------------------------------------------------------------------



#                                           abs()
#   abs() : Return the absolute value of a number The argument may be an integer, a floating point number, 
#   or an object implementing __abs__(). If the argument is a complex number, its magnitude is returned.
#   In mathematics, the absolute value of a number refers to that number's distance from zero.
#   https://www.freecodecamp.org/news/python-absolute-value-python-abs-tutorial/

number_to_abs = -15
abs_number = abs(number_to_abs)
print(abs_number)
print("-----------------------------------------------------------------------------------")
#                                               
#   any() : The any() function takes an iterable as the argument, and returns True so long as at least one of the items 
#   in the iterable is True 


list_any_1 = [0,0,0,0,0,0,1,0]
print("The first any list is :", any(list_any_1))

list_any_2 = [0,0,0,0,0,0,0,0]
print("The second any list is :", any(list_any_2))

list_any_3 = ["","","","",""]
print("The third any list is :", any(list_any_3))

list_any_4 = ["","not empty","","",""]
print("The fourth any list is :", any(list_any_4))
print("-----------------------------------------------------------------------------------")

#   all() : The all() function takes an iterable as the argument, returns True only if all items 
#   in the iterable evaluate to True or if the iterable is empty. In all other cases, the all() function returns False
#   https://www.freecodecamp.org/news/python-any-and-all-functions-explained-with-examples/

list_all_1 = [0,0,0,0,0,0,1,0]
print("The first all list is :", all(list_all_1))

list_all_2 = [0,0,0,0,0,0,0,0]
print("The second all list is :", all(list_all_2))

list_all_3 = [1,1,1,1,1,1,1,1]
print("The third all list is :", all(list_all_3))

list_all_4 = [True, False, False, False]
print ("The fourth all list is :", all(list_all_4))

list_all_5 = [True, True, True, True, True]
print ("The fourth all list is :", all(list_all_5))
print("-----------------------------------------------------------------------------------")

#                                           ascii()
#   ascii() : Replace a non-printable character with its corresponding ascii value and returns it 

non_printable_character = "Loïc"
print(ascii(non_printable_character))

print("The ascii() value of Loïc is", ascii("Loïc"))
print("-----------------------------------------------------------------------------------")
#return : 'Lo\xefc'
#                                           bin()
#   bin() : Converts a specified integer number to its binary representation and returns it
#   https://www.programiz.com/python-programming/methods/built-in/bin

integer_to_bin = 25
print(bin(25))

print("The binary representation of 25 is",bin(25))
print("-----------------------------------------------------------------------------------")

#                                           bool()
#   bool() : Return a boolean value of True or False. If x is false or omitted bool(x) will return False, 
#   otherwise it'll return True
#   https://www.programiz.com/python-programming/methods/built-in/bool

bool_test = 1
print("If our argument is not empty and non null it'll return",bool(bool_test))

bool_test2 = ""
print("If our argument is empty or null, it'll return" ,bool(bool_test2))
print("-----------------------------------------------------------------------------------")

#                                           breakpoint()
#   breakpoint() : The breakpoint() function calls sys.breakpointhook(). By default sys.breakpointhook() calls pdb.set.trace().
#   breakpoint() provide convenience in using a built-in debugger because we don't have to import the pdb module. 
#   When running breakpoint() the Pdb console will open-up.
#   https://www.digitalocean.com/community/tutorials/python-breakpoint



#                                           bytearray()
#   The bytearray() function return a bytearry object. It can convert objets into bytearray objects, or create empty bytearray
#   of the specified size. The bytearray can be used to store a collection of binary data, for example the contents of a file.
#   The downside to bytearray() is that the file content must be loaded into memory

print("The usage of bytearray() with 4 return :", bytearray(4))
print("-----------------------------------------------------------------------------------")


#                                           bytes()
#  The bytes() function is used to manipulate binary data within the program. It is used to convert an object to an immutable 
#  byte object of the given size and data. 

byte_int = 55
print ("Using byte with an integrer of 55 :", bytes(byte_int))
print("-----------------------------------------------------------------------------------")


#                                           callable()
#  The callable() function return True if the object argument appears callable and False if not.
#  even if callable(x) return x = true, the object may still be not callable, but if it return x = false, the object
#  will certainely not be callable

callable_test = 5
print("Callable test with the ojebt '5':", callable(callable_test))

def TestFunctionCallable():
    print("Test")

callable_test_2 = TestFunctionCallable
print("Callable test with the object 'def TestFunctionCallable':", callable(callable_test_2))
print("-----------------------------------------------------------------------------------")

#                                          chr() & ord()
#  chr(i) return the string whose Unicode point to the integrer i

print("The chr() function for the integrer 45 is : ", chr(45))
print("The chr() function for the integrer 66 is : ", chr(66))
print("-----------------------------------------------------------------------------------")

#   ord() return the string representing whose integrer point to a Unicode

print("The ord() function for the Unicode '-' return :", ord("-"))
print("The ord() function for the Unicode '-' return :", ord("B"))
print("-----------------------------------------------------------------------------------")

#                                           classmethod()
#  Transform a static method into a class method. A class method is a method that is bound to a class rather than its object.
#  The difference between a static method and a class method is: 
#  Static method knows nothing about the class and just deals with the parameters. 


#                                           compile()
#  Transform a static method into a class method. A class method is a method that is bound to a class rather than its object.
#  The compile() method computes the Python code from a source object and returns it.

""" codeInString = 'a = 8\nb=7\nsum=a+b\nprint("sum =",sum)'
codeObject = compile(codeInString, 'sumstring', 'exec')

exec(codeObject) """
print("-----------------------------------------------------------------------------------")

# Output: sum = 15

#                                           complex()
#  The complex() method returns a complex number (real + imaginary) when provided with a [real] parameter and an [imaginary] parameter
#  The syntax of complex() is: complex([real[, imag]])

#  Imaginary numbers are defined as the square root of the negative numbers where it does not have a definite value. 
#  It is mostly written in the form of real numbers multiplied by the imaginary unit called “i”.

complex_test = complex(2, -3)
print(complex_test)
print("-----------------------------------------------------------------------------------")

#                                           delattr() & getattr() & setattr() & hasattr()
#   The delattr() function delete the named attribute, provided the object allow it.
#   https://www.programiz.com/python-programming/methods/built-in/delattr


class delattr_test:
    dellatr_uno = "1"
    dellatr_duo = "2"
    dellatr_trece = "3"

delattr_test_01 = delattr_test()
print("Before dellatr() is used :")
print(delattr_test_01.dellatr_uno)
print(delattr_test_01.dellatr_duo)
print(delattr_test_01.dellatr_trece)

delattr(delattr_test, "dellatr_uno")

print("After dellatr() is used :")
print(delattr_test_01.dellatr_duo)
print(delattr_test_01.dellatr_trece)
print("-----------------------------------------------------------------------------------")

# The getattr() function return the value of the named attribute. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is returned.

class getattr_test:
    getattr_uno = "1"
    getattr_duo = "2"
    getattr_trece = "3"

getattr_test_01 = getattr_test

attribute_to_get = getattr(getattr_test_01, "getattr_uno")
print(attribute_to_get)
print("-----------------------------------------------------------------------------------")

#The setattr() function set the value of an object

class setattr_test :
    setattr_uno = "1"
    setattr_duo = "2"
    setattr_trece = "3"

setattr_test_01 = setattr_test()
print("The first attribute is : ", setattr_test_01.setattr_uno)
setattr(setattr_test_01, "setattr_uno","51")
print("The first attribute is : ", setattr_test_01.setattr_uno)
print("-----------------------------------------------------------------------------------")

#The hasattr() method returns true if an object has the given named attribute and false if it does not.

class hasattr_test :
    hasattr_name = "Mbappe"
    hasattr_city = "Paris"
    hasattr_club = "PSG"

hasattr_test_01 = hasattr_test()

print("Player's name is", hasattr_test_01.hasattr_name)
print("Player's name is:", hasattr(hasattr_test_01, "hasattr_name"))
print("Player's city is:", hasattr_test_01.hasattr_city)
print("Player's city is:", hasattr(hasattr_test_01, "hasattr_city"))
print("Player's club is:", hasattr_test_01.hasattr_club)
print("Player's club is:", hasattr(hasattr_test_01, "hasattr_club"))
print("Player's ballon d'or is:", hasattr(hasattr_test_01, "hasattr_ballonor"))

print("-----------------------------------------------------------------------------------")

#                                           dict()
#   The dict() function creates a dictionary. 
#   A dictionary is a collection which is unordered, changeable and indexed.
#   A dictionary can also be created with {} : b = {'one': 1, 'two': 2, 'three': 3}

dict_01 = dict(one=1, two=2, three=3)
print("This is the first dictionnary :", dict_01)
dict_02 = {"four":4, "five":5, "six":6}
print ("This is the second dictionnary :", dict_02)
print("-----------------------------------------------------------------------------------")

#                                           dir()
#   Without arguments, return the list of names in the current local scope. 
#   With an argument, attempt to return a list of valid attributes for that object.
#   https://www.programiz.com/python-programming/methods/built-in/dir


dir_test_01 = 51
print("Print dir() with the object 'dir_test_01' as an argument")
print(dir(dir_test_01))
print("Print dir() with an empty argument")
print(dir())
print("-----------------------------------------------------------------------------------")

#                                           divmod()
#   The divmod() method takes two numbers as arguments and returns their quotient and remainder in a tuple.

result = divmod(8, 3)

print("Quotient and Remainder = ",result)
print("-----------------------------------------------------------------------------------")

#                                           enumerate()
#   Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.

numbers_to_enumerate = ["1","2","3","4"]
list_to_enumerate = enumerate(numbers_to_enumerate)
print(list(list_to_enumerate))

#  The =x argument can be used to determine at which number to start enumerate

numbers_to_enumerate = ["1","2","3","4"]
list_to_enumerate = enumerate(numbers_to_enumerate, start=3)
print(list(list_to_enumerate))
print("-----------------------------------------------------------------------------------")

#                                           eval()
#   The eval() method parses the expression passed to this method and runs python expression (code) within the program.

number_to_eval = 9
square_number_to_eval = eval("number_to_eval * number_to_eval")
print ("The square of 9 is", square_number_to_eval)
print("-----------------------------------------------------------------------------------")

#                                           exec()
#   The exec() method executes a dynamically created program, which is either a string or a code object.

program_to_ex = "a = 3\nb = 3\nprint('a & b = 3 the sum of a + b =', a+b)"
exec(program_to_ex)
print("-----------------------------------------------------------------------------------")

#                                           filter()
#   The filter() function selects elements from an iterable (list, tuple etc.) based on the output of a function.
#   The function is applied to each element of the iterable and if it returns True, 
#   the element is selected by the filter() function.
#   https://www.programiz.com/python-programming/methods/built-in/filter

def check_even(numbers_to_filter):
    if numbers_to_filter % 2 == 0:
          return True  

    return False

numbers_to_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers_iterator = filter(check_even, numbers_to_filter)

even_numbers = list(even_numbers_iterator)

print("The even numbers are:", even_numbers)

print("-----------------------------------------------------------------------------------")

#                                           float()
#   The float() method returns a floating point number from a number or a string.

number_to_float = 14
float_number = float(number_to_float)
print(float_number)

print(float(11))
print(float(11.258))


print("-----------------------------------------------------------------------------------")

#                                           format()
#   The format() method returns a formatted representation of the given value controlled by the format specifier.
#   https://www.programiz.com/python-programming/methods/built-in/format

number_to_format = 45

#   The 'b' is a format type to transform the int input into binary
#   https://www.programiz.com/python-programming/methods/string/format#numbers

binary_number = format(number_to_format, 'b')
print(binary_number)

print("-----------------------------------------------------------------------------------")


#                                           frozenset()
#   Frozen set is just an immutable version of a Python set object.
#   While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
#   Due to this, frozen sets can be used as keys in Dictionary or as elements of another set.
#   But like sets, it is not ordered (the elements can be set at any index).

print("-----------------------------------------------------------------------------------")

#                                           globals()
#   The globals() method returns a dictionary with all the global variables and symbols for the current program.
#   The globals() method doesn't take any parameters.

print(globals())
print("-----------------------------------------------------------------------------------")


#                                           hash()
#   The hash() method returns the hash value of an object if it has one. 
#   Hash values are just integers that are used to compare dictionary keys during a dictionary look quickly.

text_to_hash = "There's no good kebab restaurant in my city"

hashed_text = hash(text_to_hash)
print("The text before being hashed :", text_to_hash)
print("The text after being hashed :", hashed_text)
print("-----------------------------------------------------------------------------------")

#                                           help()
#   The help() function invoke the built-in help system. (This function is intended for interactive use.) 
#   If no argument is given, the interactive help system starts on the interpreter console. 
#   If the argument is a string, then the string is looked up as the name of a module, function, class, method, 
#   keyword, or documentation topic, and a help page is printed on the console. 
#   If the argument is any other kind of object, a help page on the object is generated.

""" help(print) """
print("-----------------------------------------------------------------------------------")

#                                           hex()
#   The hex() function convert an integer number to a lowercase hexadecimal string prefixed with “0x”. 

print("This is the hex() of 23 :", hex(23))
print("-----------------------------------------------------------------------------------")

#                                           id()
#   The id() method returns a unique integer (identity) of a passed argument object.

print("The id of hasattr_test_01 is:",id(hasattr_test_01))
print("The id of binary_number is:",id(binary_number))
print("The id of hashed_text is:",id(hashed_text))
print("-----------------------------------------------------------------------------------")


#                                           input()
#   The input() function takes input from the user and returns it.

""" input_to_take = input("Enter your favorite kebab sauce : ")
print(input_to_take)
if input_to_take == "algérienne":
    print("Yes it's the only choice")
else: print("You need to try the sauce algérienne") """
print("-----------------------------------------------------------------------------------")



print("int() of 55 is : ", int(55))
print("int() of 55.5 is :", int(55.5))
print("-----------------------------------------------------------------------------------")


#                                           isinstance()
#   The isinstance() function checks if the object (first argument) is an instance or 
#   subclass of classinfo class (second argument).

class is_instance_class:
    is_instance_variable = 0

is_instance_instance = is_instance_class()

print(isinstance(is_instance_instance, is_instance_class))
print(isinstance(is_instance_class, (list, tuple)))
print("-----------------------------------------------------------------------------------")

#                                           issubclass()
#   The issubclass() function checks if the object (first argument) is a subclass 
#   of classinfo class (second argument).

class super_class_human:
    legs = True

class human_class_organs(super_class_human):
    heart : True

class class_fish:
    Fins = True

print("Is human_class_organs a subclass of super_class_human :", issubclass(human_class_organs, super_class_human))
print("Is class_fish a subclass of super_class_human :", issubclass(class_fish, super_class_human))
print("-----------------------------------------------------------------------------------")

#                                           iter()
#   The iter() method returns an iterator for the given argument. The Next parameters can be used  to iterate
#   the next item of the iterator

cities_to_iter = ["Dallas", "Venice", "Sofia", "Paris"]
iter_cities = iter(cities_to_iter)

print(next(iter_cities))
print(next(iter_cities))
print(next(iter_cities))
print(next(iter_cities))
print("-----------------------------------------------------------------------------------")

#                                           len()
#   The len() function returns the number of items (length) in an object.

length_of_cities = len(cities_to_iter)

print("This is the number of cities in my list :", length_of_cities)
print("-----------------------------------------------------------------------------------")

#                                           list()
#   The list() constructor returns a list in Python.

text_to_list = "This will be a list"
list_of_text = list(text_to_list)
print(list_of_text)
print("-----------------------------------------------------------------------------------")

#                                           locals()
#   The locals() method returns a dictionary with all the local variables and symbols for the current program.
#   The locals() method doesn't take any parameters.

print(locals())
print("-----------------------------------------------------------------------------------")

#                                           map()
#   The map() function applies a given function to each element of an iterable (list, tuple etc.) 
#   and returns an iterator containing the results.
#   The map() function takes two arguments: the function and the iterable


numbers_to_map = [2, 4, 6, 8, 10]

def square_to_map(numbers_to_map):
    return numbers_to_map * numbers_to_map

squared_numbers_to_map = map(square_to_map, numbers_to_map)

mapped_and_squared = list(squared_numbers_to_map)
print("2, 4, 6, 8, 10 squared are :", mapped_and_squared)
print("-----------------------------------------------------------------------------------")

#                                           max()
#   The max() function returns the largest item in an iterable. 
#   It can also be used to find the largest item between two or more parameters.

numbers_to_max = [1, 45, 278, 3269, 22]
max_numbers = max(numbers_to_max)
print("The largest number in my list is :", max_numbers)

numbers_to_max_2 = [4, 577894, 23, 14, 548]
list_max_numbers = max(numbers_to_max, numbers_to_max_2)
max_numbers_of_two = max(list_max_numbers)
print("The largest number within my lists is :", max_numbers_of_two)
print("-----------------------------------------------------------------------------------")

#                                           memoryview()
#   Return a “memory view” object created from the given argument.
#   https://www.programiz.com/python-programming/methods/built-in/memoryview

print("-----------------------------------------------------------------------------------")

#                                           max()
#   The min() function returns the smallest item in an iterable. 
#   It can also be used to find the smallest item between two or more parameters.

numbers_to_min = [1, 45, 278, 3269, 22]
min_numbers = min(numbers_to_min)
print("The smallest number in my list is :", min_numbers)

numbers_to_min_2 = [4, 577894, 23, 14, 548]
list_min_numbers = min(numbers_to_min, numbers_to_min_2)
min_numbers_of_two = min(list_min_numbers)
print("The smallest number within my lists is :", min_numbers_of_two)
print("-----------------------------------------------------------------------------------")

#                                           next()
#   The next() function returns the next item from the iterator.

to_next = (1, 2, 3, 4, 5)
iterator_to_next = iter(to_next)
to_next_1 = next(iterator_to_next)
print(to_next_1)
to_next_2 = next(iterator_to_next)
print(to_next_2)
to_next_3 = next(iterator_to_next)
print(to_next_3)
print("-----------------------------------------------------------------------------------")

#                                           object()
#   The object() function returns an empty object.
#   You cannot add new properties or methods to this object.
#   This object is the base for all classes, it holds the built-in properties and methods which are default for all classes.

test_object = object()

print(type(test_object))
print(dir(test_object))
print("-----------------------------------------------------------------------------------")

#                                           oct()
#   The oct() function returns an octal string from the given integer number.

# decimal to octal
print('oct(10) is:', oct(10))

# binary to octal
print('oct(0b101) is:', oct(0b101))

# hexadecimal to octal
print('oct(0XA) is:', oct(0XA))
print("-----------------------------------------------------------------------------------")

#                                           open()
#   The open() function returns a file object which can used to read, write and modify the file.
#   https://www.programiz.com/python-programming/methods/built-in/open

print("-----------------------------------------------------------------------------------")

#                                           pow()
#   The pow() method computes the power of a number by raising the first argument to the second argument

print("5^2 is :", pow(5,2))
print("-----------------------------------------------------------------------------------")

#                                           print()
#   The print() function prints the given object to the standard output device (screen) or to the text stream file.

print("Hello World")
print("-----------------------------------------------------------------------------------")

#                                           property()
#   property() returns the property attribute from the given getter, setter, and deleter.
#   If no arguments are given, property() returns a base property attribute that doesn't contain any getter, setter or deleter.
#   If doc isn't provided, property() takes the docstring of the getter function.
#   https://www.programiz.com/python-programming/methods/built-in/property

print("-----------------------------------------------------------------------------------")

#                                           range()
#   The range() function returns a sequence of numbers between the give range.
#   The range() function can take a maximum of three arguments: range(start, stop, step)

#Simply range from 0 to 3 (4 is not included)
numbers_to_range_1 = range(4)
print(list(numbers_to_range_1))  

#Range from 1 to 9
numbers_to_range_2 = range(1, 10)
print(list(numbers_to_range_2))

#Range from 4 to -10, decreasing -2 by -2
numbers_to_range_3 = range(4, -11, -2)    
print(list(numbers_to_range_3))  
print("-----------------------------------------------------------------------------------")

#                                           repr()
#   The repr() function returns a printable representation of the given object.

numbers_to_repr = [74, 75, 76, 77, 78]

printable_repr = repr(numbers_to_repr)
print(printable_repr)
print("-----------------------------------------------------------------------------------")

#                                           reversed()
#   The reversed() method computes the reverse of a given sequence object and returns it in the form of a list. 
#   The reversed() method takes a single parameter: 
#   sequence_object - an indexable object to be reversed (can be a tuple, string, list, range, etc.)

string_to_reverse = "I'm gonna be reversed"

print(list(reversed(string_to_reverse)))
print("-----------------------------------------------------------------------------------")

#                                           round()
#   The round() function returns a floating-point number rounded to the specified number of decimals.
#   The round() function takes two parameters:
#   number - the number to be rounded
#   ndigits (optional) - number up to which the given number is rounded; defaults to 0

#Simply round a number
number_to_round = 25.23
rounded_number = round(number_to_round)
print(rounded_number)

#Round a number to the given number of decimal places
print(round(15.6588, 2))
print("-----------------------------------------------------------------------------------")

#                                           set()
#   The set() function creates a set in Python.

set_01 = {21, 22, 23, 24, 25}
print(set_01)

set_02= {31, 32, 33, 34, 35, "trente six"}
print(set_02)
print("-----------------------------------------------------------------------------------")

#                                           set()
#   The slice() function returns a slice object that is used to slice any sequence (string, tuple, list, range, or bytes).
#   slice() can take three parameters:
#   start (optional) - Starting integer where the slicing of the object starts. Default to None if not provided.
#   stop - Integer until which the slicing takes place. The slicing stops at index stop -1 (last element).
#   step (optional) - Integer value which determines the increment between each index for slicing. Defaults to None if not provided.

string_to_slice = "Hello I'm gonna be sliced"
sliced_string = slice(7)
print(string_to_slice[sliced_string])
print("-----------------------------------------------------------------------------------")

#                                           sorted()
#   The sorted() function sorts the elements of a given iterable in a specific order (ascending or descending) 
#   and returns it as a list.sorted() can take a maximum of three parameters:
#   iterable - A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
#   reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
#   key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.

numbers_to_sort = [2, 15, 27, 10, 11]
sorted_numbers = sorted(numbers_to_sort)
print(sorted_numbers)
print("-----------------------------------------------------------------------------------")

#                                           staticmethod()
#   The staticmethod() built-in function returns a static method for a given function.
#   staticmethod() is considered a un-Pythonic way of creating a static function. 
#   Hence, in newer versions of Python, you can use the @staticmethod decorator.
#   One of the main benefits of using static methods in Python is that they can be called without creating an instance of the class.

class Calculator:
    def multiply_numbers(number_1, number_2):
        return number_1 * number_2
    
    
#Convert multiply_numbers() to a static method
Calculator.multiply_numbers = staticmethod(Calculator.multiply_numbers)
result_of_multiply = Calculator.multiply_numbers(3, 3)
print("9x9 is equal to :", result_of_multiply)
print("-----------------------------------------------------------------------------------")

#                                           str()
#   The str() method returns the string representation of a given object.

str_name = str("John")
str_age = str(25)
str_city = str("Dallas")

print(str_name,"is", str_age,"and live in", str_city)
print("-----------------------------------------------------------------------------------")

#                                           sum()
#   The sum() function adds the items of an iterable and returns the sum.
#   The sum() function can take two parameters :
#   iterable - iterable (list, tuple, dict, etc). The items of the iterable should be numbers.
#   start (optional) - this value is added to the sum of items of the iterable. The default value of start is 0 (if omitted)

numbers_to_sum = [55, 23, 24, 72]
sum_numbers = sum(numbers_to_sum)
print(sum_numbers)
print("-----------------------------------------------------------------------------------")

#                                           super()
#   The super() builtin returns a proxy object (temporary object of the superclass) 
#   that allows us to access methods of the base class.
#   https://realpython.com/python-super/
print("-----------------------------------------------------------------------------------")

#                                           tuple()
#   In Python, a tuple is an immutable sequence type. One of the ways of creating tuple is by using the tuple() construct.

#tuple from list
tuple_to_print = tuple([1,2,3,4])
print(tuple_to_print)

#tuple from a string
tuple_to_print_2 = tuple("This is a tuple")
print(tuple_to_print_2)

#tuple from dictionnary
tuple_to_print_3 = tuple({1:"one",2:"two",3:"three",4:"four"})
print(tuple_to_print_3)
print("-----------------------------------------------------------------------------------")

#                                           type()
#   The type() function either returns the type of the object or returns a new type object based on the arguments passed.

number_to_check_type = [2, 3, 4, 5, 6]
check_type = type(number_to_check_type)
print(check_type)
print("-----------------------------------------------------------------------------------")

#                                           vars()
#   The vars() method returns the __dict__ (dictionary mapping) attribute of the given object.

print(vars(tuple))
print("-----------------------------------------------------------------------------------")

#                                           zip()
#   The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.

sauces = ["algerienne", "biggie", "dallas", "samurai"]
viandes = ["mouton", "agneau", "boeuf", "kebab"]

zip_results = zip(sauces,viandes)
print(tuple(zip_results))
print("-----------------------------------------------------------------------------------")

#                                           __import__()
#   The function imports the module name, potentially using the given globals and locals to determine how 
#   to interpret the name in a package context.
#   Use of __import__() is Discouraged
#   This __import__() function is not necessary for everyday Python program. It is rarely used and often discouraged.
#   This function can be used to change the semantics of the import statement as the statement calls this function. 
#   Instead, it is better to use import hooks.
#   And, if you want to import a module by name, use importlib.import_module().
print("-----------------------------------------------------------------------------------")