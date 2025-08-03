#file handling 
#External data read or write or append using python program
# file handling : 
# r : read mode 
# w : write mode 
# a : append mode 
import sys 

def main():
    # open the file in r mode 
    f = open('demo.txt','r') 
    # read the content
    data = f.read()
    # finally close the file 
    print(data)    
    f.close()
    
    
sys.exit(main())

    
