#wap in python to make utility program
# streamlite run app.py 
# pip install streamlite

# python p5.py <command>

import sys 
from collections.abc import Iterable

def info():
    tmp =  ""
    
    for i in range(len(allowed_commands)): #0 to 5
        tmp = tmp + f'{i+1}. {allowed_commands[i]} \n'



    print(f'''
        info command:
        I will info with the commands.
        list of commands\n{tmp}
    ''')


def sum():
    #py p5.py sum 10 20
    total = 0
    for element in argv[2:]:
        total = total +eval(element)
    print(total)
    
    
def minus():
    #py p5.py minus 10 20
    total = 0
    for element in argv[2:]:
        total = total - eval(element)
    print(total)
    
def version():
    print('1.0.0')

argv = sys.argv
argc = len(sys.argv)

command = argv[1]
allowed_commands  = ['info','sum','minus','version','multiply','division']
if command in allowed_commands:
    eval(command+"()")
else:
    print('Invalid Command')