
l = [1,2,3,4]

d = {}

for x in l:
    d[x] = x**2
    
print('squared:',d)

#using dictionary comprehension
d1 = {x:x**2 for x in l}
print('squared: d1',d1)
