from employee import Employee
class Manager(Employee):
    def __init__(self, id, first_name, last_name, age, department, salary, managed_department):
        self.managed_department = managed_department
        super().__init__(id, first_name, last_name, age, department, salary, managed_department)

    @classmethod
    def get_all_managers(cls):
        managers = cls.db_handler.get_all_managers() 
        for manager in managers:
            print("Manager id:",manager[0])
            print("Manager name:",manager[1], manager[2])
            print("Manager department:",manager[3])
            print("Manager age:",manager[4])
            print("Manager salary: confidential")
            print("***********************************")


manager_one = Manager('8','nehad','osman', 24 ,'open-source', 800, 'web')
# manager_one.insert()
# Manager.get_all_managers()