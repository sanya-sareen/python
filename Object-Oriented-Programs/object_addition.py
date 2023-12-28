class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        total_pages = self.pages + other.pages
        return total_pages

b1 = Book(100)
b2 = Book(200)
b3 = Book(500)
print(b1+b2)
print(b1+b3)
print(b2+b3)
# b1+b2+b3 => not possible