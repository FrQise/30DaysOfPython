import re
# 30 Days of Python
# Day 18

#LEVEL 1
#1 What is the most frequent word in the following paragraph?

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

words = re.findall(r'\w+\b',paragraph)

word_counts = {}
for i in set(words):
    word_counts[i] = words.count(i)
sorted_words_by_count = sorted(word_counts.items(), key=lambda word: word[1], reverse=True)

print(sorted_words_by_count)

print("------------------------------------------")

#2 Extract these numbers from this whole text and find the distance between the two furthest particles.

txt = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

numbers = re.findall(r'-?\d+',txt)
positions = list(map(int,numbers))
distance = abs(positions[-1] - positions[0])
print(positions)
print(distance)

print("------------------------------------------")

#LEVEL 2
#1 Write a pattern which identifies if a string is a valid python variable


keyword_list = ["False","await","else","import","pass","None","break","except","in","raise","True","class","finally","is","return","and","continue","for","lambda","try","as","def","from","nonlocal","while","assert","del","global","not","with","async","elif","if","or","yield"]
banned_format = r'^[a-zA-Z][a-zA-Z0-9_]*$'

def is_valid(var_name):
    if var_name in keyword_list:
        return f"{var_name} is not a valid variable name (reserved keyword)"
    
    if not re.match(banned_format, var_name):
            return f"{var_name} is not a valid variable name"
    
    return f"{var_name} is a valid variable name"

test_if_ok = "test_if_valid"
print(is_valid(test_if_ok))

print("------------------------------------------")

#LEVEL 3
# Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean = re.sub(r'[^\w ]',"",sentence)
print(clean)

words_to_count = re.findall(r'\b\w+\b', clean)

counted_words = {}
for i in set(words_to_count):
    counted_words[i] = words_to_count.count(i)
words_counted = sorted(counted_words.items(), key=lambda word: word[1], reverse=True)
print(words_counted[:3])