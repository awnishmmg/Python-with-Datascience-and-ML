#concept of HOF
#Argument : <class 'function'>
#return : <class 'function'>

def b():
    print('b is executing')
    return 10

def a(b):
    print('a body started')
    print('type of b,',type(b))
    
    res = b()
    print('res of b:',res)
    print('type of res',type(res))
    
    print('a body ended')
    return b
    
    
result = a(b)
print('result from a:',result)
print('type of result:',type(result))
