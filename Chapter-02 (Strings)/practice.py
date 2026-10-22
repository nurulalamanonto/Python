#Question on slicing
#Take input and print middle 3 characters & last 2 charcter

str = input("Enter a string: ")
mid = len(str)//2
output1 = str[mid-1:mid+2]
print(output1)

output2 = str[-2:]
print(output2)