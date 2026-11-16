class Rect:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth

    def area(self):
        ar=self.l*self.b
        return ar

    def perimeter(self):
        p=2*(self.l+self.b)
        return p


x1=int(input("Enter length of 1st rectangle:"))
y1=int(input("Enter breadth of 1st rectangle:"))
r1=Rect(x1,y1)
print("Area of 1st rectangle:",r1.area())
print("Perimeter of 1sr rectangle",r1.perimeter())

x2=int(input("Enter length of 2st rectangle:"))
y2=int(input("Enter breadth of 2st rectangle:"))
r2=Rect(x2,y2)
print("Area of 1st rectangle:",r2.area())
print("Perimeter of 1sr rectangle",r2.perimeter())


if(r1.area()==r2.area()):
    print("\nAreas of both rectangle are same..")
else:
    print("\nAreas of both rectangle are not same..")
