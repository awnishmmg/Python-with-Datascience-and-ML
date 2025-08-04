#zipped data structure using list append method

names = ['ravi','krishna','kunal']
scores = [50,40,30,40]

m = min(len(names),len(scores))

l =  []

for i in range(m):
    n=names[i]
    s=scores[i]
    t=(n,s)
    l.append(t)
    
    

print(l)

