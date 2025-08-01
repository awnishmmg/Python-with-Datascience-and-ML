# How to run finite loop using cyclic calling 

#default argument
import sys


def loop(i,limit=100):
    #terminating condition : base condition
    if(i==limit):
        print('Hello i=',i)
        sys.exit() #return
    else: #race condition
        print('Hello i=',i)
        i = i+1
        loop(i)
    
# n=100 (n-1) => same => 99 1 => different   
def main():

    loop(1)
    
    
    
sys.exit(main())