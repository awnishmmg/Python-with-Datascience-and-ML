#zipped data structure 
# un-equal

names = ['ravi','krishna','aman','kundan']
scores = [50,40,70]

print(type(names))
print(len(names))

print(type(scores))
print(len(scores))

zipped_ns  = zip(names,scores)
print(zipped_ns)
print(type(zipped_ns))

print(list(zipped_ns))
