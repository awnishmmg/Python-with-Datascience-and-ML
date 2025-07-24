#wap in python to show use : without match

#Traditional way without match 
# python : 3.x 
# using match
# tuple matching

x = int(input("Enter the cordinates x:"))
y = int(input("Enter the cordinates y:"))

#point = x,y
point = (x,y)


match point:
    case (0,0):
        print('At Origin')
    case _:
        print('Out of the Origin')
        
     