# 1d array 
# scaler computations :
# as the heavy computation increase 
# time also increases linearly.
# Draw the graph for the 10 possible values.

import time
import sys

n=1_00_000
x_arr =  range(10,100,10) #0,1,2,3,4,5,....10

def compute(x):
    sqaures = []
    l = list(range(n))
    start = time.time()
    for i in range(len(l)):
        sqaures.append(l[i]**x)
    end = time.time() 
    y = round(end-start,2)
    return y


y_arr = []
def main(): 
    for x in x_arr:
        y_arr.append(compute(x))
        
    zipped_cordinates = zip(x_arr,y_arr)
    print(type(zipped_cordinates))
    print(list(zipped_cordinates))   

sys.exit(main())


    
