class Person:
    def __init__(self, name, dd, mm, yyyy):
        print("Person object creation....")
        self.name = name
        self.dob = self.Dob(dd,mm,yyyy)

    def info(self):
        print("Name:",self.name)
        self.dob.display()

    class Dob:
        def __init__(self,dd,mm,yyyy):
            print("DOB object creation...")
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy

        def display(self):
            print('DOB=={}/{}/{}'.format(self.dd, self.mm, self.yyyy))

p = Person('Sanya',16,6,1998)