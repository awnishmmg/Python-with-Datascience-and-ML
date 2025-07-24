#wap in python to find sum and avg or mean at compile time

import sys 
from collections.abc import Iterable

argv = sys.argv
argc = len(sys.argv)

total =  0

if isinstance(argv,Iterable):
    #print(True)
    for element in argv[1:]:
        total = total + eval(element)
    print(f'sum  of {argc-1} elements: ',total)
    print(f'Average of elements: ',total/(argc-1))
    
else:
    print(False)

