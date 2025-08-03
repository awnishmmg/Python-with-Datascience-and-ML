#file handling 
# External data read or write or append using python program
# file handling : 
# r : read mode 
# w : write mode 
# a : append mode 

# context Manager : manage the scope or context for some operation 
# it automatically assign scope as soon as you entire its block 
# it automatically release close the scope as soon leave the block.
# predinfed context manager : with clause

# other uses of with clause 
# management management
# file handling 
# database connecting
# other context management

import sys 

def main():

   # open the file in r mode 
   with open('demo.txt','r') as f:
        # read the content
        data = f.read()
        print(data)    

    
sys.exit(main())

    
