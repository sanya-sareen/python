class Test:
    __x = 10

    def __init__(self):
        self.__x = 10

    def __m1(self):
        print("It is a private method")

    def m2(self):
        print(self.__x)
        self.__m1()

t = Test()
t.m2()

