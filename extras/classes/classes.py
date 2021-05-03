# See the following for more details on Python: https://www.w3schools.com/python/default.asp.
# See the following for more details on classes: https://www.w3schools.com/python/python_classes.asp.
# See the following for mode details on the __init__(): https://www.w3schools.com/python/gloss_python_class_init.asp.
# See the following for mode details on super(): https://www.w3schools.com/python/ref_func_super.asp.

import os
import sys

class Parent():

    def __init__(self, name=""):
        self.__name = name
    
    def getName(self):
        return self.__name

    def setName(self, name=""):
        self.__name = name

class Child(Parent):

    def __init__(self, name=""):
        super().__init__(name)


def main():

    grace = Parent("Grace")

    print("{}".format(grace.getName()))

    bob = Child("Bob")

    print("{}".format(bob.getName()))

    return 0


if __name__ == "__main__":

    sys.exit(main())