from hr import PayrollSystem
from productivity import ProductivitySystem
from employees import EmployeeDatabase
import json

""" productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()

employees = employee_database.employees()
productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees) """

def print_json(d):
    print(json.dumps(d, indent=2))

employees = EmployeeDatabase().employees()

for employee in employees:
    print_json(employee.to_dict())
