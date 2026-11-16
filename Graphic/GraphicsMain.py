from Graphics.rectFuctions import *
from Graphics.cirFunctions import *
from Graphics.DGraphics.cubFunctions import *
from Graphics.DGraphics.sphFunctions import *

l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
print("Area of Rectangle: ",rectArea(l,b))
print("Perimeter of Rectangle: ",rectPerimeter(l,b))

r=int(input("Enter radius of circle:"))
print("Area of Circle: ",circleArea(r))
print("Perimeter of Circle: ",circlePerimeter(r))

r=int(input("Enter radius of sphere:"))
print("Area of Sphere: ",sphArea(r))
print("Perimeter of Sphere: ",sphPerimeter(r))

l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
h=int(input("Enter height:"))
print("Area of Cuboid: ",cubArea(l,b,h))
print("Perimeter of Cuboid: ",cubPerimeter(l,b,h))

