y1=int(input("Enter starting year:"))
y2=int(input("Enter ending year:"))

if y1>y2:
    print("End year is greater than or equal to starting year.")
else:
    print(f"Leap year from {y1} to {y2}")
    for year in range(y1,y2+1):
        if(year%4==0 and year%100!=0) or (year%400==0):
            print(year)
