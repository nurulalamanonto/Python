#If a file does not exist and we open it and write it, the file is created automatically.

file = open("report.txt", "w")
file.write("This is created to write something on a newly created file")

