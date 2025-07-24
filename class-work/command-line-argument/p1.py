#wap in python to show command line argument


import sys 

argv = sys.argv
argc = len(sys.argv)
typ = type(argv)

print('Argument variable:',argv) #['p1.py',a,b,c,d,10,20,30]
print('Argument count:',argc) #n 
print('Argument type:',typ) #list 