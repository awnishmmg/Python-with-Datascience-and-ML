#wap in python to show combination of default with keywords.
def fun(*args,a):
    print(args)
    print(a)
		

#fun(10) #invalid : 1 argument is expected
fun(10,a=20)
fun(a=10)

#default argument.
def func(*args,a=30):
    print('args=',args,'a=',a)
		

func(10,20,a=50)
func(10,a=50)
func(a=50)
func()
