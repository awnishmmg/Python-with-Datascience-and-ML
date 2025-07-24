#wap in python to show format string and raw string 

print('line will change next line')
print('line will change \n next line') #escape character \n : new line 
print('line will change \t tabbed line') #\ t: tabbed 
print('Awnish kumar') 
print('Awnish\b\b\b kumar')  #escape character sequence : \b : backspace
print("Statement 1 \n statement 2")
name = 'awnish' #single qoute
gf = "katrina"  #double qoute 
wife = ''' sunny leonne''' #triple single qoute 
brother = """ johny sins """ #triple double qoute 

print(type(name))
print(type(gf))
print(type(wife))
print(type(brother))

arr = ["8pm","blender","magic moment","black dog","bagpiper"]
print(arr)
print(type(arr)) #<class 'list'>

print('List :'+str(arr))

#format specifier
y=10
print(" name = {},y={}".format('awnish',y))
print(" name = {}, y={} ".format('awnish',20)) #order is important

print(" name = {}, y={} ".format(20,'awnish')) #order change
                                   #0,1 
print(" name = {1}, y={0} ".format(20,'awnish')) #order change with index

print(" name = {age}, y={name} ".format(age=20,name='awnish')) #order change with key and value
print(" name = {age}, y={name} ".format(name='awnish',age=20))
print(" name = {name}, age={age} ".format(name='awnish',age=20)) #format method
name = 'ravi'
age = 27
print(f'name = {name} and age = {age}') #format string 

#print('name = {name}, age={age}, {},{1},{2},{}'.format(10,20,30,name=name,age=age))
#cannot switch b/w field numering and manual value
#print(f' name = {name} and age : {age}, x={x},y={y},z={z}'.format(x=10,y=20,z=30))


#raw : kaccha
print(r' This is new\nline ') #raw 
print(r'c:\images\katreena.png') # backslash it should be with raw string

#same combination not allowed
# '' inside '' not allowed 
# "" inside "" not allowed 
# ''' inside ''' not allowed 
# """ inside """ not allowed

print("Awnish's   Gf is Katreena")  #valid 
print('Awnish\'s   Gf is Katreena') #invalid

print(" \"All that shines is not a gold said By\" -- Baba Awnish")





































