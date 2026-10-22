#Append something on a file

file = open("report.txt", "a")
file.write("\nThis is the 2nd append")

file = open("report.txt", "r")
data = file.read()
print(data)