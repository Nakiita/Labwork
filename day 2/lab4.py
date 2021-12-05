#N students take K apples and distribute them among each other evenly.The remaining apple(the indivisible)part 
students = int(input("enter the number of students"))
apple = int(input("enter the number of apples"))
a = apple // students
b = apple % students
print(f"apple each students will get :{a}")
print(f"apple remains in the basket:{b}")