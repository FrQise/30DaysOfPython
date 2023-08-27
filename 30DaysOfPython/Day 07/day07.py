#30 Days of Python
#Day 07

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#LEVEL 1

#1 Find the length of the set it_companies

print(len(it_companies))

#2 Add 'Twitter' to it_companies

it_companies.add("Twitter")
print(it_companies)

#3 Insert multiple IT companies at once to the set it_companies

it_companies.update(["Instagram","Meta","Intel"])
print(it_companies)

#4 Remove one of the companies from the set it_companies

it_companies.remove("Meta")
print(it_companies)

#5 What is the difference between remove and discard

#Answer : remove return an error if the item to remove is not found in the set, discard will not return an error

#LEVEL 2

#1 Join A and B

C = A.union(B)
print(C)

#2 Find A intersection B

print(A.intersection(B))

#3 Is A subset of B

print(A.issubset(B))

#4 Are A and B disjoint sets

print(A.isdisjoint(B))

#5 Join A with B and B with A

A.update(B)
B.update(A)
print(A)
print(B)

#6 What is the symmetric difference between A and B

print(A.symmetric_difference(B))

#7 Delete the sets completely

del(A)
del(B)

#LEVEL 3

#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age_set = set(age)
print("This is the length of the list 'age' :", len(age),"\nThis is the length of the set 'age' :", len(age_set))

#2 Explain the difference between the following data types: string, list, tuple and set
#Answer :
""" A string is a sequence of characters
A list is a dynamic sized array, they're written between [], are mutable, can store any type of element and are ordered
A tuple is the same as a list but is written between () and are immutable
A set is written between {} and unlike the list and the tuple it does not allow duplicate elements, it is mutable and unordered """

#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

str_to_split = "I am a teacher and I love to inspire and teach people"
print("There are",len(set(str_to_split.split())),"unique words in the sentence")