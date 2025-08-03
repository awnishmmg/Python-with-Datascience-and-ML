#decorator concept

def trans_decorator(func):
    def wrapper():
        print('Wrapping with Saree')
        func()
        print('Put Lali Lipstick')
        print('Hyye Hyye')
    return wrapper
        
        
@trans_decorator
def awnish():
    print('This this Awnish')
    print('Clapping Good')
  
@trans_decorator
def bansal():
    print('This this bansal')
    print('Clapping Bad')  
    
@trans_decorator
def saad():
    print('This this saad')
    print('Clapping Average')    

print('========Before Decorator======')
awnish()
bansal()
saad()

     
