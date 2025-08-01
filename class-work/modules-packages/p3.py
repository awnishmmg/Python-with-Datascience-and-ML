#module aliasing
import p1 as p 

print(p)
print(p)
print(type(p))
print(id(p)) #memory Address of p1

p.a 
p.wish()
p.add(10,20)

t = p.Test()
t.display()
