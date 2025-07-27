#wap in python to tuple unpacking

x=10,20,30
print(type(x))
print(x)


*x,y=10,20,30  #to many item unpack

print(type(x))
print(x)

print(type(y))
print(y)

#x,y,z = 10,20
*x,y=(10,20,30)  #to many item unpack

print(type(x))
print(x)

print(type(y))
print(y)


#x,y,z = 10,20
x,*y=(10,20,30)  #to many item unpack

print(type(x))
print(x)

print(type(y))
print(y)
