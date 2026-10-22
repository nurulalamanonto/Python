#This is a program for exception handling

try:
    with open("hungry.txt", "r") as f:
        f.write("I am so hungry")
except:
    print("This file doesn't exist 🥺")