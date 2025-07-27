employee_list = [
   {
	'id':1001,
	'name':'ravi',
	'dept':'HR',
	'salary' : 5000
},
{
	'id':1002,
	'name':'Anand',
	'dept':'Engineer',
	'salary' : 10000
},
{
	'id':1003,
	'name':'sandeep',
	'dept':'Finance',
	'salary' : 7000
}
]

updates_list = [ {**emp,'salary':emp['salary']+emp['salary']*0.10} 
                  for emp in employee_list
               ]
               
print('old employee:',employee_list)

print('\n\n\n\n')

print('new employee:',updates_list)
