#wap in python to create the dynamic list of odd number using range collection 

n = int(input('Enter the n value:'))
l = list(range(1,n))
print(l)

odds = []
evens = []

for i in l:
    if(i%2==1):
    #odd
        odds.append(i)
    else:
    #even 
        evens.append(i)
        
print('Odd:',odds)
print('evens:',evens)