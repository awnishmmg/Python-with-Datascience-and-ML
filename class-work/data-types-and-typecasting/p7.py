#wap in python to show the Primitive datatypes :-

from collections.abc import Iterable
x=10
print(type(x))
y=10.55555555
print(type(y))
z=10.55555555555555555555555555555555555
print(type(z))
s = 'awnish'
print(type(s))
print(len(s))

ch = 'a'
print(type(ch))
print(len(ch))

# Using Ordinality (order/ascii)
# Using Characternality (char)

print(ord(ch)) #97
print(chr(97)) #a

#print(ord(s)) #ascii to string 

def isChar(ch):
    if isinstance(ch,str) and len(ch) == 1:
        return True
    return False

print('character :',isChar('a'))
print('character :',isChar('abc'))
print(isinstance(s,Iterable))
print(isinstance([10,20,30],Iterable))
print(isinstance(10,Iterable))  

isPagal = True
print(type(isPagal))

z=10+3j
print(type(z)) #complex 

data = None 
print(type(data)) #NoneType 
















