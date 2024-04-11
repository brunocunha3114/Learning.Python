
# #number to string exemple
# days_in_jan = 31
# print ( str (days_in_jan) + " days in january")

# #String to number 

# today = 24
# remaining_days = int(days_in_jan) - today
# print("The month end's in " + str(remaining_days))

#remaining Days program
day_in_the_month = input("How many days are in this month? ")
today = input ("Wich day it is today? ")
remaining = int (day_in_the_month) - int(today)
print( f"There are {remaining} days remaining in this month.")