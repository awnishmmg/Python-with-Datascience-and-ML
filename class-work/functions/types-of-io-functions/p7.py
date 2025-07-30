#wap in python to return with collection : list

import sys

#declaration
def power(args,p):
    return [x**p for x in args]
    
   
def main():
   l = [int(x) for x in input('Enter the numbers:').split() ]
   p = eval(input('Enter the Power:'))
   result = power(l,p=p)
   print(result)
   
   
sys.exit(main())
