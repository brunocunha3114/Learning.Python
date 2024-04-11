x = int(input ("The numerator "))
y = int (input ("The denominator "))



try:
    print (x/y)
except ZeroDivisionError as e:
    print ("Not allowed to divide by zero")
else:
    print("Error not identified")
finally:
    print ("Try something else") 