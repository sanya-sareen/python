class P:
    a = 10
    def __init__(self):
        print("Parent constructor")

    def m1(self):
        print("Parent instance method")

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print("Parent static method")

class C(P):
    def __init__(self):
        print("Child constructor")

    def method1(self):
        print(self.a)
        self.m1()
        self.m2()
        self.m3()
        super().__init__()

c = C()
c.method1()
