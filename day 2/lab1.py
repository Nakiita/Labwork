# convert seconds to day, hours, minutes and seconds

s= int(input("enter the value of second:"))
Day =(((s /60)/60)/24)
print(f"total day for given seconds:{Day}")
Hour =((s /60)/60)
print(f"total minutes for given seconds:{Hour}")
Minute = (s/60)
print(f"total minutes for given seconds:{Minute}")