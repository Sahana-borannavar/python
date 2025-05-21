'''
def add(x,y):
    print(f"Addition of {x} and {y} is {x+y}")
    #print('Addition is ',x+y)
def sub(x,y):
    print(f"Difference of {x} and {y} is {x-y}")
def mul(x,y):
    print(f"Product of {x} and {y} is {x*y}")
def div(x,y):
    print(f"Division of {x} and {y} is {x/y}") # u can use floor division (//) also
'''

from first import *
import second as s
# we taking alias bcz in both modules m1 is present if we mention without taking as  it reads the updated module
m1()
s.m1()