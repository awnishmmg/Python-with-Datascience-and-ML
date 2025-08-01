#member import we can alias them 
# Now you can only access using, alias name

from p1 import a as b,add as total

print('memory id of a =>',id(b))
print('memory id of add =>',id(total))

print('a:',b) 
print('result:',total(10,20))
