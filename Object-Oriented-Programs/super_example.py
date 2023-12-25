class P:
    def m1(self):
        print("Parent method")

class C(P):
    def m1(self):
        # self.m1() # this line will throw erro, as we are trying to call m1 method of class P
        super.m1() # to avoid error we have to use super keyword to call the method of Parent class.
        print("Child method")

c = C()
c.m1()
