#wap in python to range data type and frozenset

s = {10,20,30}
print(type(s)) #set 

fs = frozenset(s)
print(type(fs))

x = range(10)
print(x)
print(type(x))


def hello():
    pass 
    
print(type(hello))

#list comprehension
z=[x for x in range(10)]
print(z)
print(type(z)) #list 

y=(x for x in range(10))
print(y)
print(type(y)) #generator

class Test:
    pass 

t = Test()
print(type(Test))
print(isinstance(t,Test))
print(isinstance(str,Test))

class User:
    pass 
    
print(type(User))














