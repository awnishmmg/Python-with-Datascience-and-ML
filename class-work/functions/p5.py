#wap in python to show the use case default argument
#default argument with position argument


def add(a,b,c=0):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    
#add() #Expected positional argument = 2
      #0
add(10,20) #argument = 2
add(10,20,30) 

add()