#wap in python as demo of **kwargs or **kwlist
#wap in python to create dynamic dictionary using list

def f1(k,v):
    print(type(k)) #key
    print(type(v)) #value
    print(k,v)
    d = {}
    
    if(len(k) == len(v)):
        for i in range(len(k)):
            key = k[i]
            value = v[i]
            d[key] = value
    else:
        print('Invalid Dictionary')
       
    print('dictionary:',d)    

f1(['name','class','marks'],['ravi','Btech',80])

