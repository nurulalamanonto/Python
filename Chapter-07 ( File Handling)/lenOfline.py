#Write a program that Read all the lines and length of the lines of a txt file

with open("fileHandling.txt", "r") as f:
    readLines = f.readlines()
    print(readLines)
    print("Number of lines: ",len(readLines))