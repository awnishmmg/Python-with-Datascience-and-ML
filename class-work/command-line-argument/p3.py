#wap in python to concetenate argument compile time


import sys 
from collections.abc import Iterable

argv = sys.argv
argc = len(sys.argv)

total =  ""

if isinstance(argv,Iterable):
    #print(True)
    for element in argv[1:]:
        total = total + element
    print(f'sum  of {argc} elements: ',total)
    
else:
    print(False)

