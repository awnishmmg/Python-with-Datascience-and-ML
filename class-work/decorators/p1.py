#functiona aliasing 

def f():
    print('f is executing...')
    
    

print(type(f)) #<class 'function'>
print(f)
print(id(f))

x=10
y=x 
print('add of x:',id(x))
print('add of y:',id(y))

d = f
f();
d();

