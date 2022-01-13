from cmath import pi

print("This will determine the volume of a cylinder, given diameter and height (in metres)")
diameter = float(input("Enter diameter: "))
radius = diameter/2
height = float(input("Enter height: "))
volume = pi*(radius*radius)*height
print("The volume of this cylinder is ", round(volume, 2) , "m2")