#functiona aliasing 

def f():
    print('f is executing...')


d = f
f()
d();

print('stack Address of d:',id(f))
print('stack Address of f:',id(d))

del f;
#print(f) #invalid
print(d)

