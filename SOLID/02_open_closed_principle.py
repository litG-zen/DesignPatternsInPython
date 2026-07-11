# Open-Closed principle is a design principle that states that software entities (classes, modules, functions, etc.) 
# should be open for extension but closed for modification.
# This means that you should be able to add new functionality to a class without changing its existing code.  

from enum import Enum 

class Size:
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Color:
    RED = 1
    GREEN = 2
    BLUE = 3


# Antipattern Example
# Here the Product class is violating the open-closed principle because if we want to add a new filter criteria,
# we would have to modify the existing code of the Product class.
class Product:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p
    
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p
    
    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p

# Open class pattern Example
class Specification: # BaseClass 
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)
    
class Filter: # BaseClass 
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item
    
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))

class OrSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return any(map(lambda spec: spec.is_satisfied(item), self.args))

class ImprovedFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    tesla = Product("Tesla", Size.MEDIUM, Color.GREEN)
    iphone = Product("Iphone 15", Size.SMALL, Color.BLUE)
    villa = Product("Penthouse", Size.LARGE, Color.BLUE)

    products = [tesla, iphone, villa]

    print("Green products (old):")
    pf = Product("", 0, 0)
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is green")

    print("Green products (new):")
    bf = ImprovedFilter()
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name} is green")

    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is large")

    print("Large and blue products:")
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")
    
    print("Large or blue products:")
    large_or_blue = OrSpecification(large, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_or_blue):
        print(f" - {p.name} is large or blue")