#%%
import os
import sys

#%%
class Parent():
    def __init__(self, name="Parent"):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name="Parent"):
        self.__name = name

#%%
class Child(Parent):
    def __init__(self, name="Child"):
        self.__name = name

#%%
grace = Parent()

print(grace.getName())

#%%
bob = Child()

print(bob.getName())

#%%
class Child(Parent):
    def __init__(self, name="Child"):
        super().__init__(name)

#%%
bob = Child()

print(bob.getName())

# %%
