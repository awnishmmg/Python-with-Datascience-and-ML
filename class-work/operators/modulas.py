#wap in python to show, ternary 
#wap in python to implement modolus functions 
# y= f(x)= |x| = { 1. if x>0 => x 2. if x<0 => -x }
# y=|-5| => 5
# y=|5| => 5

x = eval(input('Enter x:'))
result = x if(x>0) else (-x)
print(f' y=|{x}| = {result}')


