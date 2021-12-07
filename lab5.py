#	A student will not be allowed to sit in exam if his/her attendance is less than 75%.
a= int(input("enter a number of classes held "))
b= int(input("enter a number of classes attended"))
percentage =b/a*100
if percentage>=75:
    print("the students are allowed to sit in exam")
else:
    print("the students are not alloweed to sit in exam")
