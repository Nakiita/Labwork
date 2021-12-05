#You live 4 miles from university.The bus drives at 25mph but spends 2 minutes at eaach of the 10 stops on the way.How long will the bus
#  journey take? Alternatively, you could run to university. You jog the first mile at 7mbph then run the next two at 15mnbph; before
#  jogging the last at 7mbph again. Will this be quicker or slower than bus?

distance = 4
speed1 = 25
stop_T = 10*2
time = 1/speed1
time2 = time*60
total_time =time2+stop_T
print(f"the total time to reach university by bus{total_time}")
speed2=7
time1=1/speed2
time_1=time1*60
speed3=15
time2=2/speed3
time_2=time2*60
speed4=7
time3=1/speed4
time_3=time3*60
total_time2=time_1+time_2+time_3
print(f"the total time foe walking is {total_time}")
print(f"walking is faster to reach university{total_time2}")