import requests
import collections
import re
import statistics

# 30 Days of Python
# Day 20

#1 Read this url and find the 10 most frequent words

print("#1")
# book_text = requests.get("https://www.gutenberg.org/cache/epub/63107/pg63107.txt").text
# word_pattern = re.compile(r'\b\w+\b')
# book_word_counter = collections.Counter(word_pattern.findall(book_text))
# # for word, count in book_word_counter.most_common(10):
#     # print(f"{word} : {count}")

print("------------------------------------------")

#2 Read the cats API and find the min, max, mean, median, standard deviation of cats' weight in metric units.

print("#2")

cats_api = 'https://api.thecatapi.com/v1/breeds'
cats_request = requests.get(cats_api)
cats_data = cats_request.json()
all_weights = []
for cat in cats_data:
    weight_data = cat.get('weight', None)
    if weight_data:
        metric_weight = int(weight_data['metric'].split()[0]) 
        all_weights.append(metric_weight)

min_weight = min(all_weights)
max_weight = max(all_weights)
mean_weight = statistics.mean(all_weights)
median_weight = statistics.median(all_weights)
standard_deviaiton_weight = statistics.stdev(all_weights)
print(f"Minimum: {min_weight}. Maximum : {max_weight}. Mean : {mean_weight}. Median : {median_weight}. Standard Deviation : {standard_deviaiton_weight}")

print("------------------------------------------")

#3 Create a frequency table of country and breed of cats
print("#3")

#Not sure I'm gonna finish this day, the link are mostly dead, it's a pain and I don't freaking know what is a frequency table