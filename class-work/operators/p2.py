#wap in python working with Math module 
# even though python provides, native operators  but they restricted to few mathematical operations
# hence python provides math library which is built on native c langauge 
# 1. python different flavours 
# 1. python + .net => iron python 
# 2. python + java => jython
# 3. python(2.x) + python(3.x) => pypy 
# 4. python + c langauge = cpython
 

import math as m
import sys
# factorial 
print(m.factorial(5)) #120 
#print(m.factorial(100))
#print(m.factorial(500))
#print(m.factorial(2000))

# what is range if digit of factorial 4300
# Yes we can increase it 
#sys.set_int_max_str_digits(200000)
print(m.ceil(3.5)) # 4
print(m.ceil(3.1)) # 4
print(m.ceil(3.9)) # 4

print(m.floor(3.5)) # 3
print(m.floor(3.1)) # 3
print(m.floor(3.9)) # 3

print(m.ceil(3)) #3
print(m.floor(3)) #3
print(m.ceil(2)==m.floor(2)) #True 

#fmod 
print(m.fmod(5,2))
# if x > y : return float(x%y)
# if y > x : return float(x)
print(m.fmod(5,6))
print(abs(-5)) # modulus|absolute value
print(abs(5)) # modulus|absolute value

#logarithmic 
print(m.log(2)) 
print(m.log2(8))
print(m.log10(100))

#trignometry and inverse 
#sin sinh
print(m.sin(30))
print(m.sinh(30))

#infinite 
print(m.inf)
print(m.nan)
print(m.pi) #3.14

#round 
print(round(2.543,2))


#type check operator in math module 
print(m.isnan(10))
print(m.isinf(10))
print(m.isinf(10))













