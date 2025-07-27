#wap in python to : v-arg method (variable n)
#variable length argument.
# with positional Argument 
# position < keyword < default < varg(*dynamic) < double dynamic(**)[kwargs](double vargs)

#with positional
def func(a,*col):
    print(a)
    print(type(a))
    print(col)
    print(len(col))
    print(type(col))
    
#func  
#func()
func(10)
func(10,20,30)
#func(a=20,30,10)
#func(20,30,a=10)
#func(,30,20,40,a=10)





