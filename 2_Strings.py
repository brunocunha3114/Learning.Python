firstname = "Bruno"
lastname = "Cunha"


#first option 
output = "hello " + firstname + " " + lastname 
print (output)


#second
output = "hello {} {}". format(firstname,lastname)
print(output)


#third
output = "hello {1} {0}". format(firstname,lastname)
print(output)


#forth and fancier ahah
output = f"hello {firstname} {lastname}"
print(output)
