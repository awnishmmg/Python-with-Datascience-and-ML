#concept of nested functions
def a():
    
  print('a body started')
  def b():
	  print('b body started')
	  print('b body ended') 
  b()
  print('a body ended')



a()

