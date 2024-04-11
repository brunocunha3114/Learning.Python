from datetime import datetime, timedelta

# today = datetime.now() 
# print ("today is " + str(today.day))

birthday = input ("What is your birthday (dd/mm/yyyy)? ")
today = datetime.now()
birthday_date = datetime.strptime(birthday, "%d/%m/%Y")

days = today - birthday_date

years_old = 

print(f"So you have {years_old}")