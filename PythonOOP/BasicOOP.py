#Create Class
class Employee:
    #Create Mothod
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print("Employee name = {}".format(self.name))
        print("Salary = {}".format(self.salary))
        print("Department = {}".format(self.department))

obj1=Employee()
