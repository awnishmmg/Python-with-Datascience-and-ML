#wap in python as demo dynamic dictionary using dictionary comprehension,list comprehension
#wap in python to create dynamic dictionary using list

def f1(*k,v):
    print(type(k)) #key
    print(type(v)) #value
    print(k,v)
    
    d = {k[i]:v[i] for i in range(len(k))}       
    print('dictionary:',d)    

f1('name','class','marks',v=('ravi','Btech',80))

