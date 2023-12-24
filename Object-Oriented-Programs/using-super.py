class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def project_name(self):
        print("Working on Python project")

class Employee(Person):
    def __init__(self, name, age, eno, sal):
        super().__init__(name,age)
        self.eno = eno
        self.esal = sal

    def work(self):
        print("Working in google")

    def emp_info(self):
        print("Employee name:", self.name)
        print("Employee age:", self.age)
        print("Employee number:", self.eno)
        print("Employee salary:", self.esal)

e = Employee('Sanya',78,99000,123123)
e.project_name()
e.work()
e.emp_info()
