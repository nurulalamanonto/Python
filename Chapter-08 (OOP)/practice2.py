#Using class and object doing average of 3 subject marks of a student

class student:
    def __init__(self,name,listOfMarks):
        self.name = name
        self.listOfMarks = listOfMarks

    def avg(self):
        sum = 0
        for eachVal in self.listOfMarks:
            sum = sum+eachVal
        average = sum/3
        print(f"Average of marks is: {average:.2f}")


s1 = student("Nurul", [85,88,95])
s1.avg()

#If we use @staticmethod before def__init__() method we don't need use self anymore
#This is used for utility level functions