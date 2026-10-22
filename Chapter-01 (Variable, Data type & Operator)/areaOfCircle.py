#Calcualte the area of a circle
import math
diameter = int(input("Enter the circle diameter: " + "\n"))
radius = float((diameter/2))
print("The radius of the circle is: ", radius, "\n")
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area:.4f}",)