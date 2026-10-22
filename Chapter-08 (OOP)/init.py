# The __init__ function runs automatically whenever an object is created.
# It is used to initialize attributes

class student:

    def __init__(self, name, id):
        self.name = name
        self.id = id

s1 = student("Nurul", "23240")
s2 = student("Naeem", "23241")

print("Student 1,","\nName:",s1.name," ID: ", s1.id)
print("Student 2: ","\nName:",s2.name," ID: ", s2.id)

#If we use @staticmethod before def__init__() method we don't need use self anymore
#This is used for utility level functions