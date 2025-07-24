#wap in python to show Bitwise :-
#wap in python to swap a numbers 
# 4. using XOR (Exclusive Or)


a = eval(input('Enter the a value:'))
b = eval(input('Enter the b value:'))
print(f'Before swap : a={a} and b={b}')
a = a^b
b = a^b
a = a^b 
print(f'After swap : a={a} and b={b}')