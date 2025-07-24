#wap in python to show use : without match

#Traditional way without match 
# python : 3.x 
# using match

ch = input("Enter the character:")

match ch.lower():
    case 'a':
        print('vowel')
    case 'i':
        print('vowel')
    case 'e':
        print('vowel')
    case 'o':
        print('vowel')
    case 'u':
        print('vowel')
    case _:
        print('consonant')
     