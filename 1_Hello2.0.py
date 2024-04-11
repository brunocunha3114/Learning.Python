#Let's upgrade my first code
First_name = input ("What is your first name? ")
Last_name = input ("What is your last name? ")
Letter = "A"
output = f"Hello {First_name.capitalize()} {Last_name.capitalize()}!!! \nHave a good day"
print (output)
print("")
A = First_name.count("a") + Last_name.count("a") + First_name.count("A") + Last_name.count("A") 
output = f"Did you know you have {A} letter's '{Letter}' in your name"
print (output)
