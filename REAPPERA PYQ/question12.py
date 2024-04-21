class Parent:
    def __init__(self, lst):
        self.list = lst

    def evenEle(self):
        return [num for num in self.list if num % 2 == 0]

class Child(Parent):
    def oddEle(self):
        return [num for num in self.list if num % 2 != 0]

# Taking input
input_list = [int(x) for x in input().split()]

# Creating Child object
child = Child(input_list)

# Printing even and odd elements
print(child.evenEle())
print(child.oddEle())
