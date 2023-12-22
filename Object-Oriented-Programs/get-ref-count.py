import sys

class Test:
    pass

t = Test()
print("reference count",sys.getrefcount(t))