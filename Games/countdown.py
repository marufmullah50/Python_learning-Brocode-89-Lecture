import time
# to sleep  time.sleep(3) 
# slipped for 3 seconds
my_time= int(input("Enter number of times to be counted down in seconds: "))
i = 1
for i in range(my_time, 0, -1):
    seconds = int(i%60)
    minutes = int((i/60)%60)
    hours = int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)  # Sleep for 1 second between prints
print("Times Up")
