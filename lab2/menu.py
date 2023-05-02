from employee import Employee
from manager import Manager


def Menu():
    flag = True
    while flag:
        print("## List all Employees, enter 'list'")
        print("## Add Employee, enter 'add'")
        print("## Fire Employee, enter 'fire'")
        print("## Exit: enter q")
        value = input()
        if value == 'list':
            employee_type = input("Are you a manager or an employee? Enter 'm' or 'e': ")
            if employee_type == 'm':
                Manager.get_all_managers()
            elif employee_type == 'e':
                Employee.get_all_records()
            else:
                print("Invalid input")

        elif value == 'add':
            id = input("SSN: ")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            age = input("Age: ")
            department = input("Department: ")
            salary = input("Salary: ")
            managed_department = input("Managed Department: ")
            new_employee = Employee(id,first_name, last_name, age, department, salary, managed_department)
            new_employee.insert()

        
        elif value == 'fire':
            id = int(input("Employee ID: "))
            Employee.fire(id)
            print("*************FIRED**************")

        elif value == 'q':
            flag = False

Menu()