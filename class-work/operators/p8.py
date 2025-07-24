#wap in python to show use : without match

#Traditional way without match 
# python : 3.x 
# using match
# merging all the cases

ch = input("Enter the character:")

match ch.lower():
    case 'a'|'i'|'e'|'o'|'u': #merging cases into one.
        print('vowel')
    case _:
        print('consonant')
     