'''
single inheritance
'''

class P:
    def m1(self):
        print()

class C(P):
    def m2(self):
        print()

c = C()
c.m1()
c.m2()

'''
multi-level inheritance
'''

class A:
    def a1(self):
        print()

class B(A):
    def b1(self):
        print()

class D(B):
    def d1(self):
        print()

d = D()
d.a1()
d.b1()
d.d1()


'''
multiple inheritance
'''
class Y1:
    def m1(self):
        print("m1")

class Y2:
    def m1(self):
        print("m1")

class Y3(Y1, Y2):
    def m2(self):
        print("m2")

y = Y3()
y.m2()
y.m1()   #m1 of class Y1 would be called.
'''
hierarical inheritance-
parent 1, multiple child
'''

