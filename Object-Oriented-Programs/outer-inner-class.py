class Outer:
    def __init__(self):
        print("Outer object creation")

    class Inner:
        def __init__(self):
            print("Inner class object")

        def m1(self):
            print("Inner class method")

o = Outer()
i = o.Inner()
i.m1()

# i = Outer().Inner()
# i.m1()
