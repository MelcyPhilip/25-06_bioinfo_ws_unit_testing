import numbers
import os
import yaml

def calculator(x, y, operation):
    """perform simple mathematical operation on two numbers"""
    # check if x and y are numbers (bool is considered a number)
    if not isinstance(x, numbers.Number) or not isinstance(y, numbers.Number):
        raise TypeError("both x and y need to be numeric")
    match operation:
        case "addition":
            return x+y
        case "subtraction":
            return x-y
        case "multiplication":
            return x*y
        case "division":
            return x/y
        case _:
            raise ValueError("{} is not a valid operation".format(operation))

def read_yaml(filepath):
    """read yaml file"""
    # check if filepath belongs to existing file
    if not os.path.isfile(filepath):
        raise ValueError("{} is not an existing file".format(filepath))
    file = open(filepath)
    data = yaml.safe_load(file)
    file.close()
    return data

# develop your own function and add a unit test that covers all its test cases (exceptions included)