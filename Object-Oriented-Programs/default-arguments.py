class Test:
    def m1(self, a=None,b=None, c=None):
        if a is not None and b is not None and c is not None:
            print("Three arguments")

        elif a is not None and b is not None:
            print("Two arguments")

        elif a is not None:
            print("One argument")

        else:
            print("No argument")

t = Test()
t.m1(10,11,12)
t.m1(10,11)
t.m1()
