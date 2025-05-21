#types of variables
x=10#global variable can access both outside and inside the function
y=20#global variable
def f1():
    y=30#local variable access only inside the function
    print(x)
    print(y)
    print(globals()['x'])
    print(globals()['y'])
f1()
print('\n')

x=10
def f2():
    x=20
    print(x)
    print(globals()['x'])
f2()