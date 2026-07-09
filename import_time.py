import random
import time
times=[]
for i in range(s):
    start=time.time()
    wait=random.randint(1,3)
    time.sleep(wait)
    end=time.time()
    elasped=end_start
    times.append(elapsed)
avg=sum(times)/len(times)
print("average time=",avg)