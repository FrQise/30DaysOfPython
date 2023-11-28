import datetime
# 30 Days of Python
# Day 16

#1 Get the current day, month, year, hour, minute and timestamp from datetime module

now = datetime.datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(f"Today we are the {day},{month},{year} and it is {hour}:{minute} and the timestamp is {timestamp}.")

print("------------------------------------------")

#2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

mnth = now.strftime("%m/%d/%Y")
tme = now.strftime("%H:%M:%S")

print(f"{mnth}, {tme}")

print("------------------------------------------")

#3 Today is 5 December, 2019. Change this time string to time.

time_3 = datetime.date(2019,12,5)
print(time_3)

print("------------------------------------------")

#4 Calculate the time difference between now and new year.

today = datetime.date(2023,11,28)
new_year = datetime.date(2024,1,1)
time_left_for_newyear = new_year - today
print(time_left_for_newyear)

print("------------------------------------------")

#5 Calculate the time difference between 1 January 1970 and now.

january_oneninesevenzero = datetime.date(1970,1,1)
difference_time = today - january_oneninesevenzero
print(difference_time)