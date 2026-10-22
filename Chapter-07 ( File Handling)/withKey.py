"""Usually we use file.close() to close a file
    but if we use "with" keyword while opening a file this file automatically closes"""

with open("withKey.txt", "r") as f:
    data = f.read()
    print(data)
