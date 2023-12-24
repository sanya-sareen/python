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
hierarical inheritance-
parent 1, multiple child
'''

