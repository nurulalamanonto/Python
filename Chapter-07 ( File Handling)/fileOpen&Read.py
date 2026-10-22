#Opening a file and reading the file and printing the file data

file = open("fileHandling.txt", "r")
data = file.read()

print("Reading the file:\n",data)