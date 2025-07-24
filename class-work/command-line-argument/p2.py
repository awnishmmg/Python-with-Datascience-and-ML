#wap in python to show command line argument


import sys 
from collections.abc import Iterable
argv = sys.argv
argc = len(sys.argv)
typ = type(argv)

print(isinstance(argv,Iterable)) #loop 

for element in argv:
    print(type(element))
    
    

