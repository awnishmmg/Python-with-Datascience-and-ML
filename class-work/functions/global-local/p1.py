#wap in python  to local and global scope
import sys
a = 10
print(f' the value of a at global scope = {a}')

#@global scope 

def fun():
    global a
    #@local scope
    b = 20
    print(f' @fun => the value of a at local scope from global = {a}') #1
    print(f' @fun => the value of b at local scope from local = {b} ') #2
    a = 20
    print(f' @fun => the value of a at local scope from local = {a}') #3
    
print(f' the value of a at global scope = {a}') #4


def main():
    #@local scope
   fun()
   print(f' @main => the value of a at local scope from global = {a}')
   #print(f' @main => the value of b at local scope from local = {b} ') 
   
  
sys.exit(main())
