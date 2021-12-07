#write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.
a= int(input("enter first number"))
b= int(input("enter second number"))
c=int(input("enter third number"))
if a==b==c or a==b or a==c:
     print("The sum is 0")
else:
    print(f"the sum of three number is {a+b+c}")