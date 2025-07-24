#wap : in python to show sep and end operator;
#sep : multiple arguments
#end : at the last of the statement 

#sep  :  it sperated the multiple argument by delimeter =' ' 
print('x','y','z')
name = 'Awnish'
mname = 'Kr'
lname = 'Sharma'
print(name,mname,lname) #multiple argument : sep = ' '  Awnish Kr Sharma 
print(name,mname,lname,sep='')
print(name,mname,lname,sep='@')
print(name,mname,lname,sep='-')

#Question : Without using space How can, add  space using sep keyword.
print(name,mname,lname,sep=chr(0))  # Ascii Not allowed
print('x'+'y'+'z')
print('x','y','z')
print('x ','y ','z',sep='\b')

#end : is operator which will after the of the statement.
#end = '\n' or Enter or ascii chr(10)
print('line 1',end='.\n')
print('line 2')
print('line 3',end='')
print('line 4')

#Question : Without using end Operator display line 1,line 2 ... line 3 in different lines 

print('line 1','line 2','line 3',sep='\n') # seperator
#docstring not allowed
print('''
line 1
line 2 
line 3 
''')
print('line 1 \n line 2 \n line 3')
print('my','gf','name','katrina',end='.',sep='-')



















