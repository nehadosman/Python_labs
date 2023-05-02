import mysql.connector
from mysql.connector import Error

class MySqlHandler:
    def __init__(self, table):
        self.host= "localhost" 
        self.user = "root" 
        self.passwd = "" 
        self.port = 4306
        self.database = "python-office"
        self.table = table

    def connect(self):
        try:
            self.myconn = mysql.connector.connect(
                host = self.host,
                user = self.user,
                passwd = self.passwd,
                port = self.port,
                database = self.database,
            )
            print("connected successfully")
        except Error as e:
             print("Error connecting to MySQL database: ", e)

    # def show_all_databases(self):
    #     self.connect()
    #     mycursor = self.myconn.cursor()
    #     mycursor.execute("SHOW DATABASES")
    #     for db in mycursor:
    #         print(db)

    def insert(self, data):
        self.connect()
        mycursor = self.myconn.cursor()
        sql = f"INSERT INTO {self.table} (id, first_name, last_name, age, department, salary, managed_department) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql , data)
        self.myconn.commit()
        print("insert data done")

    def update(self, id, department):
        try:
            self.connect()
            mycursor = self.myconn.cursor()
            sql = f"UPDATE {self.table} SET department=%s WHERE id= %s"
            data = (department,id)
            mycursor.execute(sql, data)
            self.myconn.commit()
            print("updated data successfully")
        except Error as e:
            print("Error updating record: ", e)

    def delete(self, id):
        self.connect()
        mycursor = self.myconn.cursor()
        try:
            sql = f"DELETE FROM {self.table} WHERE id= %s"
            data = (id,)
            mycursor.execute(sql, data)
            self.myconn.commit()
            print("Data deleted ")
        except Error as e:
            print("Error deleting record: ", e)

    def get_all_records(self):
        self.connect()
        sql = f"SELECT * FROM {self.table}"
        try:
            mycursor = self.myconn.cursor()
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print("Employes data retrieved successfully")
            return result
        except Error as e:
            print("Error retrieving records: ", e)

    def get_all_managers(self):
        self.connect()
        sql = f"select * from {self.table} where `managed_department` != ' ' "
        try:
            mycursor = self.myconn.cursor()
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(" Managers data retrieved successfully")
            return result
        except Error as e:
            print("Error retrieving records: ", e)


