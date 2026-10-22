#Read and print a file line by line

with open("fileHandling.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()

    print("Line 1 = ",line1)
    print("Line 2 = ",line2)
    print("Line 3 = ",line3)