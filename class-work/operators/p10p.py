#wap in python to show use : without match

#Traditional way without match 
# python : 3.x 
# using match
# List matching

drinks = eval(input("Enter list:"))

match drinks:
    case ['blender']:
         print('little Drinker')
    case ['blender','black dog']:
        print('Medium Bewada')
    case ['blender','black dog','8pm']:
        print('High Level Bewada')
    case _:
        print('Very Very Very Big Bewada')   
     