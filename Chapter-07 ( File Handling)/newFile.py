#Creating a new file using "x" it will show erro if the same name file already exists

file = open("report1.txt", "x")
file.write("New file is created")

file = open("report1.txt", "x")