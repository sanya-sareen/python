class Test:
    def __init__(self):
        self._x = 10

    def m1(self):
        print(self._x)

class SubTest(Test):
    def m2(self):
        print(self._x)

t= SubTest()
t.m1()
t.m2()