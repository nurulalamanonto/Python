#Countdown Timer

import time

count = int(input("Enter the timer time: "))
print("Countdown starts from now...")

for i in range(count,0,-1):
    print(i)
    time.sleep(1)

print("Happy New Year!")