class Test:
    count = 0

    def __init__(self):
        Test.count += 1

    @classmethod
    def get_no_objects(cls):
        print("The no. of objects created",cls.count)

Test.get_no_objects()
t1 = Test()
t2 = Test()

Test.get_no_objects()