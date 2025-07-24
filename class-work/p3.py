# wap in python to demo of docstring
import sys


# user defined functions
def say_hello():
    '''
        @title : This is say Hello functions
        @author : awnish Kumar
        @created_date : 14-07-2025
        @created_at : 19:11
        @github : https://github.com/awnishmmg/python-repo.git
        @license : ISC or MIT 
    '''
    print('Say Hello')
    
#main 
def main():
    say_hello()
    #print(say_hello.__doc__) #Magic variable : docstring inside a method,class or module

#sys.exit(main())
