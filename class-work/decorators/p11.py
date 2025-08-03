#decorator concept : Type 3

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
 

trans_decorator(awnish)()
trans_decorator(bansal)()
trans_decorator(saad)()

     
