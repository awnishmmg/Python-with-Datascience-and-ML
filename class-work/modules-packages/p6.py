#member  import
# problem with member import.

from p1 import a,add

print('memory id of a =>',id(a))
print('memory id of add =>',id(add))


print('a:',a) #No Reference
print('result:',add(10,20))

#wish() # error 

from p1 import wish

wish() # it is not imported in memory.




