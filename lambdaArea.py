square_area = lambda a: a**2
rectangle_area = lambda l, b: l * b
triangle_area = lambda ba, h: 0.5 * ba * h

a = int(input("Enter the side length of the square: "))
print("Area of square:", square_area(a))

l = int(input("Enter the rectangle length: "))
b = int(input("Enter the rectangle breadth: "))
print("Area of rectangle:", rectangle_area(l, b))

ba = int(input("Enter the triangle base: "))
h = int(input("Enter the triangle height: "))
print("Area of triangle:", triangle_area(ba, h))

