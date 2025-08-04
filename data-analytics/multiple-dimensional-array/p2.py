# 1d array 
# scaler computations :
# as the heavy computation increase 
# time also increases linearly.

import time
n=1_00_000

sqaures = []
l = list(range(n))

start = time.time()

for i in range(len(l)):
    sqaures.append(l[i]**10)
    
end = time.time() 
print(f' total time =  {end-start:.2f} seconds')

    
