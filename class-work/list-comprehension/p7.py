# finding the Homogenous List 

l = ['Awnish',10,20,20.5]


print(all([True,False,False,False])) #False : str 
print(all([False,True,True,False])) # False : int
print(all([False,False,False,True])) #False : float

n_l = [isinstance(x,str) for x in l] # str
print(n_l)

print(all([isinstance(x,str) for x in l]))





