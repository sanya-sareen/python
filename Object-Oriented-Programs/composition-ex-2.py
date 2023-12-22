class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getInfo(self):
        print("Car Name:{}, Model:{}, Color:{}".format(self.name, self.model, self.color))


class Employee:
    def __init__(self, ename, eno, car):
        self.ename = ename
        self.eno = eno
        self.car = car

    def empInfo(self):


        print("Employee name:{}, Employee id:{}, Employee car details:{}".format(self.ename, self.eno, self.car))
        self.car.getInfo()


car = Car("innova","2.5",'Grey')
e = Employee('Durga',89999,car)
e.empInfo()