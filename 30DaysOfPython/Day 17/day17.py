# 30 Days of Python
# Day 17

#1 Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

fin, swe, nor, den, ice , *rest = names
nordic_countries = ', '.join([fin, swe, nor, den, ice])

es, ru = rest

print(nordic_countries)
print(es)
print(ru)