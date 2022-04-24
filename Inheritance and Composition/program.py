import json

from hr import LTDPolicy, calculate_payroll
from productivity import track
from employees import Employee, employees

def print_dict(d):
    print(json.dumps(d, indent=2))

employees_data = employees()

sales_employee = employees_data[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)

track(employees_data, 40)
calculate_payroll(employees_data)