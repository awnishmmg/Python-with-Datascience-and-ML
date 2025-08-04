# Representation of 2d list 

r1 = [10,20,30]
r2 = [40,50,60]

print('order of r1',len(r1))
print('order of r2',len(r2))

l3 = [r1,r2]

print(l3)
print('order of l3 :',len(l3)) # 2

matrix =  [
    [10,20,30],#r1
    [40,50,60] #r2
]

print('Matrix 2d',matrix)

dimension = f'{len(matrix)}x{len(matrix[0])}'

print('Matrix of order :',dimension)
