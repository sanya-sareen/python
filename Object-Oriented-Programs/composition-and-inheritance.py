class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def get_info(self):
        print("\t car name: {}, \t Model:{} \t Color:{}".format(self.name, self.model, self.color))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def projects(self):
        print("Working on various projects")

class Employee(Person):
    def __init__(self,name, age, eno,esal,car):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
        self.car = car

    def work(self):
         print("COding in python")

    def emp_info(self):
        print("Employee name:",self.name)
        print("Employee age:", self.age)
        print("Employee salary:", self.esal)

        print("Employee car info:",)
        self.car.get_info()

car = Car("Innova",'2.5zv','Grey')
e = Employee("sanya",78,244555,10000000,car)
e.work()
e.projects()
e.emp_info()