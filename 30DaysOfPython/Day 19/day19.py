import json
import re
from collections import Counter
import csv
# 30 Days of Python
# Day 18

#LEVEL 1
#1 Write a function which count number of lines and number of words in a text
print("#1")
def count_lines_words(file="30DaysOfPython\Day 19\Fondation.txt"):
    with open(file) as file:
        content = file.read()
        lines = content.splitlines()
        number_of_lines = len(lines)
        words = content.split()
        number_of_words = len(words)
        return {"lines": number_of_lines, "words": number_of_words}
    
#Read Fondation.txt and count number of lines and words

print(count_lines_words("30DaysOfPython\Day 19\Fondation.txt"))

#Read Man_In_High_Castle.txt and count nubmer of lines and words

print(count_lines_words("30DaysOfPython\Day 19\Man_In_High_Castle.txt"))

#Read The_Shining.txt and count the number of lines and words

print(count_lines_words("30DaysOfPython\Day 19\The_Shining.txt"))

print("------------------------------------------")

#2 Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

with open("30DaysOfPython\Day 19\countries_data.json", "r", encoding="utf-8") as file:
    countries_dict = json.load(file)

def most_spoken_language(data):
    language_counts = {}
    for country_data in data:
        languages = country_data.get("languages",[])

        for language in languages:
            if language in language_counts:
                language_counts[language] += 1
            else:
                language_counts[language] = 1
    sorted_languages = sorted(language_counts.items(), key=lambda lang: lang[1], reverse=True)
    return sorted_languages[:10]

print(most_spoken_language(countries_dict))

print("------------------------------------------")

#3 Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

def most_populated_countries(data):
    pop_country_list = [(country['name'], country['population']) for country in data]
    sorted_pop_country = sorted(pop_country_list, key=lambda item: item[1], reverse=True)
    return sorted_pop_country[:10]
print(most_populated_countries(countries_dict))

print("------------------------------------------")

#LEVEL 2
#1 Extract all incoming email addresses as a list from the email_exchange.txt file.

with open ("30DaysOfPython\Day 19\email_exchange.txt", "r", encoding="utf-8") as file:
    file_content = file.read()
    match = re.findall(r"#?From\s+([\w.-]+@[\w.-]+)", file_content)
    print(match)

print("------------------------------------------")

#2 Find the most common words in The_Shining.txt. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, 
# indicating the number of words. Your function will return an array of tuples in descending order. Check the output


def find_most_common_words(txt,isfile=False,posint=5):
    if isfile == True:
        openned_file = open(txt, "r",encoding="utf-8").read()
        words = openned_file
    else: 
        words = txt
    words_counts = {}
    for word in words.split():
        if word in words_counts:
            words_counts[word] += 1
        else:
            words_counts[word] = 1
    sorted_words = sorted(words_counts.items(), key=lambda word: word[1], reverse=True)
    return sorted_words[:posint]

print(find_most_common_words("30DaysOfPython\Day 19\The_Shining.txt",True,3))

print("------------------------------------------")

#3 Write a python application that checks similarity between two texts. It takes two files or two strings as a parameter and it will evaluate the similarity of the two texts.
""" 
def check_type(txt1, isfile1, txt2, isfile2):
    if isfile1 and isfile2:
        words1 = read_text(txt1)
        words2 = read_text(txt2)
    elif isfile1:
        words1 = read_text(txt1)
    elif isfile2:
        words2 = read_text(txt2)
    else:
        words1 = txt1
        words2 = txt2
    return words1, words2

print(check_type(first_text,True,second_text,True))"""

def read_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def check_type(txt, isfile):
    if isfile:
        return read_text(txt)
    return txt

def clean_text(text):
    cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    cleaned_text = re.sub(r"\s+", " ", cleaned_text)
    return cleaned_text.lower()

def remove_filtered_words(cleaned_text):
    stop_words = set(['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"])
    words = cleaned_text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)

def get_word_counts(text):
    return Counter(text.split())

def compare_word_counts(counts1, counts2):
    common_words = set(counts1.keys()) & set(counts2.keys())
    sorted_common_words = sorted(common_words, key=lambda word: counts1.get(word, 0) + counts2.get(word, 0), reverse=True)
    print("Common Words:")
    for word in sorted_common_words:
        count1 = counts1.get(word, 0)
        count2 = counts2.get(word, 0)
        print(f"{word}: Occurs {count1} times in the first text and {count2} times in the second text")


first_text = "30DaysOfPython\Day 19\MFDOOM_Doomsday.txt"
second_text = "30DaysOfPython\Day 19\MFDOOM_Figaro.txt"

compare1 = remove_filtered_words(clean_text(check_type(first_text, True)))
compare2 = remove_filtered_words(clean_text(check_type(second_text, True)))

compare_word_counts(get_word_counts(compare1), get_word_counts(compare2))

print("------------------------------------------")

#4 Read the hacker news csv file and find out: 
# a) Count the number of lines containing python or Python 

def count_python_lines(file_path):
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        python_lines = [line for line in reader if any("python" in element.lower() for element in line)]
    return len(python_lines)

csv_file_path = "30DaysOfPython\Day 19\hacker_news.csv"

print(count_python_lines(csv_file_path))

print("------------------------------------------")

#b Count the number lines containing JavaScript, javascript or Javascript

def count_javascript_lines(file_path):
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        javascript_lines = [line for line in reader if any("javascript" in element.lower() for element in line)]
    return len(javascript_lines)

csv_file_path = "30DaysOfPython\Day 19\hacker_news.csv"

print(count_javascript_lines(csv_file_path))

print("------------------------------------------")

#c Count the number lines containing Java and not JavaScript

def count_java_lines(file_path):
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        java_lines = [line for line in reader if "java" in line[1].lower() and "javascript" not in line[1].lower()]
    return len(java_lines)

csv_file_path = "30DaysOfPython\Day 19\hacker_news.csv"

print(count_java_lines(csv_file_path))