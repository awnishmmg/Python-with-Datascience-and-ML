#wap in python : factorial n=5 using sequencial calling using #step
# 5! = 5*4*3*2*1
# 5! = 1*2*3*4*5
# 5! = 5*4!
# n! = n*(n-1)!

# Recursion : 

 n=5
import sys

#1
def step1(n):
    return n*1; #1*1 => 1
  
#2 
def step2(n):
    return n*step1(n-1) #2*step1(1) = 2*1 => 2
     
#3         
def step3(n):
    return n*step2(n-1) #3*step2(2) = ? 3*2 => 6
 
#4 
def step4(n): 
    return n*step3(n-1) #4*step3(3) => ? 4*6 => 24
#5    
def main(): #Home
   
    print(n*step4(n-1)) #5*step4(4) => ? 5*24 => 120
                         
      
sys.exit(main())




