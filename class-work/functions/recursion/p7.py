#wap in python : factorial n=5 using sequencial calling using #step
# 5! = 5*4*3*2*1
# 5! = 1*2*3*4*5
# 5! = 5*4!
# n! = n*(n-1)!
# !n = n*!(n-1)
# ! = factorial
# factorial(n) = n*factorial(n-1)

#1! = 1 
#0! = 1

import sys
sys.setrecursionlimit(2000)

def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)

def main(): #Home
   n = int(input('Enter the n value:'))
   print(factorial(n))
                         
      
sys.exit(main())




