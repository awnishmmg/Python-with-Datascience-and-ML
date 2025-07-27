#wap in python to show the use case default argument
#default argument position order
#default argument must be placed at last.

def add(a,b,c=0):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    

#add(10,20) #argument = 2
#add(10,20,30) 

#keyword argument
add(c=50,a=10,b=20)