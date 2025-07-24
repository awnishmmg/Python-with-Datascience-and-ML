#wap in python to show Bitwise :-
#wap in python to swap a numbers 

# 1 using third variable
# 2. not using third variable => Mathematics 
# 3. python tuple style
# 4. using XOR (Exclusive Or)
# 5. shallow copy and deep copy 

x = eval(input('Enter the x value:'))
y = eval(input('Enter the y value:'))
print(f'Before swap : x={x} and y={y}')

#(x,y) = (y,x) #python tuple style (tuple - unpacking)

[x,y] = [y,x]
print(f'After swap : x={x} and y={y}')