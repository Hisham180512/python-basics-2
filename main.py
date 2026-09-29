# MY WEATHER REPORTER
# PART-1 USER INPUT
city = input("Enter your city name: ")
temp = float(input( "Enter today's tempreature in C: "))

#PART-2 if STATEMENT
if temp >35: 
 print("Warning its a very hot day: ")

#PART-3 if else
if temp > 25:
 print("Great day to go outside!")
else:
 print("Grab a jacket before you go out!")

#PART-4 if-elif-else
if temp > 35:
 print("Weather: Scorching hot!")
elif temp > 25:
 print("Weather: Warm and sunny")
elif temp > 15:
 print("Weather: Cool and breezy")
else:
 print("Weather: Cold - Stay warm!")

 #PART-5 datetime MODULE 

 import datetime
 import calendar

 now = datetime.datetime.now()
 print("City: ", city)
 print("Time now", now)
 print(calendar.calendar(now.year))