#wap in python to combination of position + *args + default
#default argument.

def func(b,*args,a=30):
    print('b= |',b,'|args=|',args,'a=',a)
    print()
		

func(10,20,40,a=50)
func(10,20,40)

