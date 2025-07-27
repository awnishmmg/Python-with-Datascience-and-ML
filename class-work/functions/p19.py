#wap in python as **kv or **kwargs


def f1(**kv):  
    print('dictionary:',kv)    

f1(name='Awnish',branch='cse',marks=80,wife='Sunny')

def f2(**kwargs):  
    print('dictionary:',kwargs)    
    print(type(kwargs))

f1(name='Awnish',branch='cse',marks=80,wife='Sunny')
f2(name='Awnish',branch='cse',marks=80,wife='Sunny')