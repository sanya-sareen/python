class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def display(self):
        print('Name:',self.name)
        print('Age:', self.age)
        print('Heigth:', self.height)
        print('Weigth:', self.weight)



class Student(Person):
    def __init__(self, name, age, height, weight, rollno, marks):
        super().__init__(name, age, height, weight)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print('Rollno:', self.rollno)
        print('Marks:', self.marks)

s = Student('Ravi',24,5.6,70,101,95)
s.display()