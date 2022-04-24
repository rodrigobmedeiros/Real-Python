import json

from hr import calculate_payroll
from productivity import track
from employees import Employee, employees

def print_dict(d):
    print(json.dumps(d, indent=2))

calculate_payroll(employees())
track(employees(), 40)

temp_secretary = Employee(5)
print('Temporary Secretary')
print_dict(temp_secretary.to_dict())
