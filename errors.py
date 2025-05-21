li=[10,20,30,40,50]
x=10
try:
    print(x/2)
    print(li[4])
    print(10/0)
except Exception as e: # exception - run time error
    print(e)
except:
    print('An error occurred')
print('Hello')
# by using try and exception the whole code will run
# without try and exception the code runs untill the error occurred



# using single exception
x=int(input('please enter a number: '))
try:
    print(x)
    y = [10, 20, 30]
    print(y[0])
    print(y[1])
    print(y[2])
    print(y[3])
except Exception as e:
    print(e)




#using multiple exception
print('Good Morning')
x=10
li=[1,2,3,4,5]
try:
    print(x/0)
except Exception as e:
    print(e)
try:
    print(li[5])
except Exception as e:
    print(e)



#using multiple exception
try:
    x=int(input('please enter a number: '))
    print(x)
    y = [10, 20, 30]
    print(y[0])
    print(y[1])
    print(y[2])
    print(y[3])
except ValueError:
    print('enter a valid number')
except NameError:
    print('x is invalid')
except IndexError:
    print('you are accessing wrong position')



# using multiple exception
x=[10,20,30,40,50]
y=10
try:
    print(x[0])
    print(y/0)
except IndexError: # named exception, comes b/w try and except
    print('Trying to access a non existent index')
except ZeroDivisionError: # named exception, comes b/w try and except
    print('Trying to divide a number by 0')
except: # this is default except and generic exception, it should be placed at last
    print('An error occurred')
