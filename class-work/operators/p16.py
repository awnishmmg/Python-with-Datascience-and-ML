#wap in python to show similar type in collection : Homogenous collection 

import sys
arguments = sys.argv

#print(arguments)


for i in range(len(arguments)):
    print(f'The Type of item = {arguments[i]} at Index={i} is :{type(arguments[i])} ')
    
 
print(all(arguments))
print(all([10,20,30,'Awnish',True,None]))
print(all([ isinstance(i,int) for i in [10,20,30,'Awnish']]))

print(all([True,True,True,False]))


