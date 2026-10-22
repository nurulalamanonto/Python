#Implicit Conversion

print("This is implicit part")
x = 5 #int
y = 2.5 #float
z = x+y 
print(z, "\n")

#Explicit Conversion

print("This is explicit part")
num = input("Enter a number: ")
convertVal = float(num) 

print("The original value is: ", num)
print("The type is: ", type(num), "\n")
print("The converted value is: ", convertVal)
print("The type is: ", type(convertVal))