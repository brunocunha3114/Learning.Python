country = input("where are you from? ")

if country.lower() == "canada" :
    print ("Hey you are a canadian!!!\nI have an app to calculate your tax")
    price = input ("How much did you pay? ")
    price = float (price)
    if price >= 1.00:
        tax = 0.07
    else :
        tax = 0  
    print (f"You will pay {tax} % in tax")
else :
    country = country.capitalize
    print (f"nice you are from {country}!!!\n it's such a nice country")