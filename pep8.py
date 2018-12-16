# based on: https://www.youtube.com/watch?v=Sm0wwmEwqpI
# https://pep8.org/

# variables names
my_variable = "test"

# constants names
PI_VALUE = "this is a constant value with CAPs"

# functions names
# Always leave 2 lines before and after a function


def my_function_name():
    variable = ''
    return variable


# Class names (First letter in CAP and no _)
class People:
    def __init__(self, name):
        self.name = name

    def __str__(self):

        return self.name


my_name = People(name='kesylo')
print(my_name)

# Non public proprities names of a class
_my_propriety = 'private propriety'

# Conflicting variable names
in_ = 'in'
print_ = 'print'