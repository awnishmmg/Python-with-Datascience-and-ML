#wap in python to demonstrate the sequential calling

import sys

def a(args):
    print('a called a=',args)
    d(args+5)    
        
def b(args):
    print('b is called b=',args)
    c(args+10)
     
        
def c(args):
    print('c is called c=',args)
    
    
def d(args):
    print('d is called d=',args)
    b(args+20)
    
def main():
    a(100)
    
    
sys.exit(main())




