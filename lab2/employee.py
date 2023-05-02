from database.MySql_Handler import MySqlHandler
class Employee: 
    db_table = 'employee'   
    db_handler = MySqlHandler(db_table) 

    all_employees = []
    def __init__(self, id, first_name, last_name, age, department, salary, managed_department=''):
        self.id = id
        self.fname = first_name
        self.lname = last_name
        self.age = age 
        self.department = department
        self.salary = salary
        self.managed_department = managed_department
        Employee.all_employees.append([self.id,self.fname,self.lname,self.age, self.department, self.salary, self.managed_department])


    def insert(self):
        self.db_handler = self.__class__.db_handler
        data = [self.id,self.fname,self.lname,self.age, self.department, self.salary, self.managed_department]
        self.db_handler.insert(data)

    def transfer(self, id, new_department):
        self.department = new_department
        # Employee.all_employees[id-1][3] = new_department #assume that id in database equal index of array minus 1
        for employee in Employee.all_employees:
                if employee[0] == id:
                    employee[4] = new_department
        self.db_handler = self.__class__.db_handler
        self.db_handler.update(id,new_department)

    @classmethod
    def fire(cls, id):
        cls.db_handler.delete(id) 
        cls.all_employees = [employee for employee in cls.all_employees if employee[0] != id]

    def show(self):
        print("Employee name:",self.fname,self.lname)
        print("Employee department:",self.department)
        print("Employee salary:",self.salary)
        print("Employee age:",self.age)
        print("**********************************")
        
    @classmethod
    def get_all_records(cls):
        employees = cls.db_handler.get_all_records() 
        for employee in employees:
            print(employee)

# Emp_one = Employee(15,'shady','osman', 24 ,'open-source', 800)
# # Emp_one.insert()
# Emp_two = Employee(16,'yousry','mohammed', 33,'iti', 800)
# Emp_two.show()
# # print(Employee.all_employees)
# # Emp_one.transfer(1,'web')
# Employee.fire(3)

