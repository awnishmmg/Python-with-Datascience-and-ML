#wap in python : factorial n=5 using sequencial calling using #step
# 5! = 5*4*3*2*1
# 5! = 1*2*3*4*5
# 5! = 5*4!
# n! = n*(n-1)!

import sys

def step1(n):
    print('step',n)
        
        
def step2(n):
    print('step',n)
    step1(n-1)
     
        
def step3(n):
    print('step',n)
    step2(n-1)
 
def step4(n):
    print('step :',n)
    step3(n-1)
    
def main():
     step4(5)
      
sys.exit(main())




