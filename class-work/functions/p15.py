#wap in python as demo of **kwargs or **kwlist


def f1(d):
    print(type(d))
    print(d)
    
#f1()
f1(()) #valid
f1([]) #valid
f1((10,20)) #valid 


f1({10,20}) #set
f1({})  #dictionary
f1(set())
f1({'name':'Awnish','wife':'sunny','half_wife':'katreena','hobby':['driking','driving','jailing']})

