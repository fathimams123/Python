class Time:
    def __init__(self):
        self.__hour = int(input("Enter the hour (0-23): "))
        self.__minute = int(input("Enter the minute: "))
        self.__second = int(input("Enter the second: "))

    def __add__(self, other):
        total_seconds = ((self.__hour+other.__hour)*3600+(self.__minute+other.__minute)*60+self.__second+other.__second)
        hour = (total_seconds // 3600) % 24
        minute = (total_seconds // 60) % 60
        second = total_seconds % 60
        return f"{hour:02d}:{minute:02d}:{second:02d}"


print("Enter time 1")
t1 = Time()
print("Enter time 2")
t2 = Time()
result = t1 + t2
print("Sum of 2 times:", result)
