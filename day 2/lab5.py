a = int(input("enter the number of students in first class"))
b = int(input("enter the number of students in second class"))
c = int(input("enter the number of students in third class"))
sum = a//2+b//2+c//2+a%2+b%2+c%2
print(f"total number of desks we need:{sum}")