class NestedMethods:

    def m1(self):
        def calc(a,b):
            print("The sum", a+b)
            print("The product", a * b)
            print("The difference", a - b)
        calc(10,20)

t = NestedMethods()
