class Engine:
    def __init__(self):
        self.power = "123KW"
    def useEngine(self):
        print("Engine specifiv functionality")


class Car:
    def __init__(self):
        self.engine = Engine()

    def useCar(self):
        print('car required engine functionality')
        self.engine.useEngine()
        print(self.engine.power)

c = Car()
c.useCar()