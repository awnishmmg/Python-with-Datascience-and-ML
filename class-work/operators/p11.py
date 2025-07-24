#wap in python to show membership operator 

#s1 =  "vikatkavi"

#x = input('Enter any character:')
#print(x in s1)

#print('z' not in s1) # True 

# use of in for iteration 
for i in range(5): #0,1,2,3,4
    print(i)

l = [10,20,30]
print(30 in l) # True 
print(100 in l) # False 
print(20 not in l)  # False 


user = {'name':'awnish','age':27}

#checking in keys
print('name' in user.keys())
print('age' in user.keys())
print('rollno' in user.keys())

#checking in values 
print('rahul' in user.values()) #False
print(27 in user.values()) #True
print(None in user.values()) #False


#checking in values 
print('rahul' not in user.values()) #True
print(27 not in user.values()) #False
print(None not in user.values()) #True
