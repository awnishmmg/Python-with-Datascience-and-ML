#wap in python to show type casting

x = input('Enter the 1st value:')
print('value of x:',x)
print('type of the x:',type(x)) 

y = input('Enter the 2nd value:')
print('value of y:',y)
print('type of the y:',type(y))
print('==========Before Typecasting========')
result = x+y 
print(result) 

print('==========After Typecasting========')
x = int(x) #type conversion
y = int(y) #type conversion
print('type of x:',type(x),'type of y:',type(y))
result = x+y 
print(result) 

