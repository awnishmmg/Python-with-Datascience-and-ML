#decorator concept : type 2

def trans_decorator(func):
    def wrapper():
        print('Wrapping with Saree....')
        func()
        print('Put Lali Lipstick....')
        print('Hyye Hyye...')
    return wrapper
        
       
def awnish():
    print('This this Awnish')
    print('Clapping Good')

  
def bansal():
    print('This this bansal')
    print('Clapping Bad')  



def saad():
    print('This this saad')
    print('Clapping Average')   
 

#without 
x = trans_decorator(awnish)
y = trans_decorator(bansal)
z = trans_decorator(saad) 

x()
y()
z()

     
