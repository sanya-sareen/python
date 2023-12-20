class Employee:
    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self):
        print("Employee number", self.eno)
        print("Employee name:", self.ename)
        print("employee salary:", self.esal)

class Manager:
    @staticmethod
    def updateEmp(emp):
        emp.esal = emp.esal + 10000
        emp.display()

emp = Employee(101, 'Sanya',900000)
Manager.updateEmp(emp)
