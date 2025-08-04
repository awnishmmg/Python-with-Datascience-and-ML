#zipped data structure using list append method

names = ['ravi','krishna','kunal']
scores = [50,40,30,40]

l =  []

for i in range(min(len(names),len(scores))):
    l.append((names[i],scores[i]))
    
    

print(l)

