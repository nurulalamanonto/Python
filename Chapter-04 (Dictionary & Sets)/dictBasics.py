#Uses of dictionary
student = {
    "Name" : "Nurul Alam",
    "Roll" : "22",
    "Dept" : "CSE"
}

# print(type(student))
# print(student["Name"])
# print(student)

#Adding new key in dictionary
student["ID"] = "2324022"
print(student)
#Poping any key from dict
student.pop("ID") 
print(student)
#Methods of dictionary
print(student.keys())
print(student.values())
print(student.items())