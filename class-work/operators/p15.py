#wap in python : to form validation of the form in cli without any 
# for any
import sys

def main():
    print("=================> User Registration <===================")

    name = input('Enter the Name:')
    dob = input('Enter the Dob:')
    email = input('Enter the Email:')
    mobile = input('Enter the Mobile:')
    password =  input('Enter password:')
    cnf_password = input('Enter confirm Password:')
    
    subject_1 = input('Enter the Subject 1:')
    subject_2 = input('Enter the Subject 2:')
    subject_3 = input('Enter the Subject 3:')
    
    #Condition: Student Must choose at least one subject
    subjects = [subject_1,subject_2,subject_3]
     
    user = {
        'name':name,
        'dob' :dob,
        'email':email,
        'mobile':mobile,
        'password':password,
        'cnf_password':cnf_password,
        'subject_selected':any(subjects)
    }
    
    
    if(validate(user)):
        print('Register Success')
        print('==========Display User Info==============')
        print(str(user))
    else:
        print('Any of Field is Not Filled, Please fill it')

def validate(user):
  return all(user.values()) #values
   

sys.exit(main())

   