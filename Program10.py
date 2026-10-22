list1=[8,6,7,4,5]
list2=[5,4,3,2,1]

if len(list1) == len(list2):
    print("The both list has same length")
else:
    print("The both list has different length")

print(f"Sum of list1:{sum(list1)} and Sum of list2:{sum(list2)}")

if sum(list1)==sum(list2):
    print("List sum to the same value")
else:
    print("List sum to the different value")

common_value=set(list1) & set(list2)
