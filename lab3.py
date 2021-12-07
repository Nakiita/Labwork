print("Enter age")
age = int(input())
print("Gender?(M or F)")
gender = input()
if (gender =="F" or gender == "f") and 20<=age <=60:
    print("Urban areas only")
elif (gender =='M'or gender =="m")and 40<age<=60:
    print("urban areas only")
else:
    print("ERROR")