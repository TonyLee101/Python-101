#Create Class
class Employee:
    #Create Mothod
    def detail(self,name,salary):
        self.name = name
        self.salary = salary
        print("Employee name = {}".format(self.name))
        print("Salary = ",self.salary)

obj1=Employee()
obj1.detail("Oat",20000)

obj2=Employee()
obj2.detail("Jojo",40000)