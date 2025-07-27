#wap in python to add n of argument

def summation(*col):
    print(type(col))
    print(len(col))
    print(col)
    total = 0
    for i in col:
        total = total+i
    print('total:',total)
    
    
#call 
summation() #0
summation(10) #1
summation(10,20) #2
summation(10,20,30) #3
summation(10,20,30,40) #4


