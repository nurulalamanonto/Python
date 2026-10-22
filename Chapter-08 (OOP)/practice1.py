#Create a class and add some attributes
#create 2 objects with different values

class laptop:
    brand = "Lenovo"
    ram = "8GB"
    ssd = "120GB"

laptop1 = laptop()
laptop1.brand = "Hp"
laptop1.ram = "16GB"
print("Laptop-1: ", laptop1.brand, laptop1.ram, laptop1.ssd)

laptop2 = laptop()
laptop2.brand = "Dell"
laptop2.ram = "24GB"
print("Laptop-2: ", laptop2.brand,laptop2.ram, laptop2.ssd)