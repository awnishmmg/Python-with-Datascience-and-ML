#wap in python to return with collection : unique list

import sys

#declaration
def power(args,p):
    return list(set([x**p for x in args]))
    
   
def main():
   l = [int(x) for x in input('Enter the numbers:').split() ]
   p = eval(input('Enter the Power:'))
   result = power(l,p=p)
   print(result)
   
   
sys.exit(main())
