#new year countdown timer
import time 

count=int(input("Enter count:"))
i=1

print("Countdown starts in")
for i in range(count ,0,-1):
    print(i)
    time.sleep(1)

print("HAPPY NEW YEAR")