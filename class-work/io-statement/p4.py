#wap in python to show the c formattings 

name = 'ravi'
age = 20
salary = 5500.55555 #2 floating 

print('name = %s, age=%d and salary = %f'%(name,age,salary))
print('name = %s, age=%d and salary = %.2f'%(name,age,salary))
print('name = {:s}, age={:d} and salary = {:.2f}'.format(name,age,salary))
print(f'name = {name}, age={age} and salary = {salary:.2f}')