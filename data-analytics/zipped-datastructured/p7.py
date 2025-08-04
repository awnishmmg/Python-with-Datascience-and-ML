#zipped data structure using list append method

names = ['ravi','krishna','kunal']
scores = [50,40,30,40]

l = [(names[i],scores[i]) for i in range(min(len(names),len(scores)))]
    
print(l)

