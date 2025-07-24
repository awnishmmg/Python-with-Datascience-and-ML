#wap in python : to form validation of the form in cli without using any 
# level : 0
import sys

def main():
    print("=================> User Registration <===================")

    name = input('Enter the Name:')
    dob = input('Enter the Dob:')
    email = input('Enter the Email:')
    mobile = input('Enter the Mobile:')
    password =  input('Enter password:')
    cnf_password = input('Enter confirm Password:')
    
    user = {
        'name':name,
        'dob' :dob,
        'email':email,
        'mobile':mobile,
        'password':password,
        'cnf_password':cnf_password
    }
    
    if(validate(user)):
        print('Register Success')
        print('==========Display User Info==============')
        print(str(user))
    else:
        print('Register Failed, Please correct the Error')

def validate(user):
   if user['name']=="":
        return False
   if user['dob']=="":
        return False
   if user['email']=="":
        return False
   if user['mobile']=="":
        return False
   if user['password']=="":
        return False
   if user['cnf_password']=="":
        return False
   return True
   


sys.exit(main())

   