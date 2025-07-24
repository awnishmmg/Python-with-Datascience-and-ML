#wap in python to show the similar type Operation 
import math 
a=5
print('value of a:',a)
print('type of a:',type(a))

b=2 
print('value of b:',b)
print('type of b:',type(b))

c='4'
print('value of c:',c)
print('type of c:',type(c))

print(a+b)
print(a-b)
print(a*b)
print(a/b)#float division
print(int(a/b))
print(math.floor(a/b)) #2.5 --> floor --> 2
print(a//b) #int division => floor division

print(5//2.0) # implicit typecasting 2.0
d='4'
print('value of d:',d)
print('type of d:',type(d))
print(c+d) 
print(c*a) #valid -> str*number => n of times string => string multiplication 
#print(c*3.5) ---> #incompatible type 
#print(3.5*c)
#print(c-d)  #incompatible type 
#print(c*d)  #incompatible type 
#print(c/d)  #incompatible type 
print(c+a) #incompatible type 



