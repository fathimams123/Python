#create a class rectangle with private attribute length and width.Overload '<' operator to compare the area of 2 rectangle

class Rectangle:
    def __init__(self,l,b):
        self.__length=l
        self.__breadth=b
    def getDimension(self):
        return self.__length,self.__breadth
    def getArea(self):
        return self.__length*self.__breadth
    def __lt__(self,other):
        return self.getArea()<other.getArea()

length1=int(input("Enter the length of 1st rectangle:"))
breadth1=int(input("Enter the breadth of 1st rectangle:"))

ar1=Rectangle(length1,breadth1)

length2=int(input("Enter the length of 2nd rectangle:"))
breadth2=int(input("Enter the breadth of 2nd rectangle:"))

ar2=Rectangle(length2,breadth2)


print(f"Area of 1st rectangle={ar1.getArea()}")
print(f"Area of 2nd rectangle={ar2.getArea()}")

if ar1<ar2:
    print("1st rectangle is smaller ")
elif ar1>ar2:
    print("2st rectangle is smaller ")
else:
    print("Both rectangles are equal")
