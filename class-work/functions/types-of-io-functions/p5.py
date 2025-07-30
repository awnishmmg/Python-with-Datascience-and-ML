#wap in python to show with Argument and with Return type
#dynamic 
import sys
#declaration:
def add(x,y):
    return x+y
   
   
def main():
    #calling
    x = eval(input('Enter the x value:'))
    y = eval(input('Enter the y value:'))
    
    result = add(x ,y)
    print('The sum=',result)
    
sys.exit(main())
