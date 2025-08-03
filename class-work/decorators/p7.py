#callback functions
#A function which take functions as argument, and then calls that functions within same functions 
# is called callable : ja simran jelo apni zindagi.


def calling(a,b):
    print('I am callable functions ')
    return a+b 
    
    
    

def a(callback,a,b):
    res = callback(a,b) # callback
    print('Result of a and b',res)
    
    
a(calling,10,20)





     
