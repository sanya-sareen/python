class Test:
    def m1(self, *args):
        print("Variable length arguments")

t = Test()
t.m1(10,11,12)
t.m1(10,11)
t.m1(1,2,3,4,5,6,7,8,9,0)
t.m1("Happy birthdYY")