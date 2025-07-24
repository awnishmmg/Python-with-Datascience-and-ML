#wap in python : using member operator find the frequency of the element 
# given list = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
# dictionary = {1:3,2:4,3:4,4:4}

# {1:3,2:2,3:2,4:1}
lst = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
d = {} # Empty dictionary
print(d)

for item in lst: #0 to n-1
    if item in d.keys():
        d[item] =  d.get(item)+1
    else:
        d[item] =  d.get(item,1)
print(d)
  