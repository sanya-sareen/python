class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def display(self):
        print("Hello:", self.name)
        print("Your marks are:",self.marks)

    def grade(self):
        if self.marks >= 60:
            print("first")

        elif self.marks >=50:
            print("second")


n = int(input('Enter no. of students:'))
for i in range(n):
    name = input("Enter student name:")
    marks = int(input("Enter marks:"))
    s = Students(name, marks)
    s.display()
    s.grade()
    print()