country = input("where are you from? ")
tax = 0


#Opção 1
# if country == "canada":
    
#     province = input("what province you live in? ")
    
#     if province == "alberta":
#         tax = 0.05
#      elif province == "nunavut":
#         tax = 0.13
#     elif province == "ontario":
#         tax = 0.13
#     else:
#         tax = 0,15
# else:
#     tax = 0



#Opção 2
# if country == "canada":
    
#     province = input("what province you live in? ")
    
#     if province == "alberta" or "nunavut":
#         tax = 0.05
#     elif province == "ontario":
#         tax = 0.13
#     else:
#         tax = 0,15
# else:
#     tax = 0


#Opção 3 (the best one)
if country == "canada":
    
    province = input("what province you live in? ")
    
    if province in ("alberta", \
                    "nunavut", "yukon"):
        tax = 0.05
    elif province == "ontario":
        tax = 0.13
    else:
        tax = 0,15
else:
    tax = 0


print (f"You will pay {tax} in tax")
