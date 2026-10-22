#Copying fileHandling.txt

import shutil

shutil.copy("fileHandling.txt", "copied.txt")
with open("copied.txt", "r") as f:
    data = f.read()
    print(data)