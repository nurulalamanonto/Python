"""Write a program to read text of a file and find whether it contains the word 'flow' """

file = open("fileHandling.txt", "r")
data = file.read()

data = data.lower()
if "flow" in data:
    print("Yes found")
else:
    print("Not found")