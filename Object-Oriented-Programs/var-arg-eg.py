class Test:
    def sum(self, *args):
        total = 0
        for x in args:
            total = total + x
        print("SUM:",total)

t = Test()
t.sum(1,2,3,4,5)
t.sum(88,77,886,55)
