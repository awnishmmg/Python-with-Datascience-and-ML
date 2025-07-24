#wap in python to show use : without match

#Traditional way without match 
# python : 3.x 
# when match was not there one can implement switch case using dictionary

ch = input("Enter the character:")

def switch(ch): #lower case A=> a a=>a
        #Indentation start 
        
        cases = {
            'a':'Vowel',
            'i':'Vowel',
            'o':'Vowel',
            'e':'Vowel',
            'u':'Vowel'
            
        }
        default = 'consonant'
        
        result = cases.get(ch,default)
        print(result)
        
switch(ch.lower())