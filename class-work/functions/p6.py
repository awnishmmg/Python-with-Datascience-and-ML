#wap in python to show the use case default argument
#default argument with keyword argument


def add(a,b,c=0):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    

#add(10,20) #argument = 2
#add(10,20,30) 

#keyword argument
add(a=100,b=200)
#add(a=100,b=200,30)# error position Argument must be before keyword argument
add(30,b=100,c=200)
add(30,c=100,b=200)