#wap in python to return with collection : dictionary

import sys

#declaration
def createUser(name,age,email):
    
    return {
           'name':name,
            'age' : age,
            'email':email,
            'role' : 'user',
            'password': 1234,
            'permission' : [
                {
                    'course_add':True,
                     'course_read':True,
                     'course_update': False,
                     'course_delete':False,
                },
                {
                    'lecture_add':True,
                     'lecture_read':True,
                     'lecture_update':False,
                     'lecture_delete':False,
                }
            ]
    }
   
   
def main():
    #calling
    name = input('Enter the name:')
    age = input('Enter the age:')
    email = input('Enter the email:')
    
    created_user  = createUser(name,age,email)
    if(len(created_user)> 0):
        print('user created successfully :',created_user)
    else: 
        print('User Error')
    
sys.exit(main())
