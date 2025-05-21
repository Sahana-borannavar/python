class Details:
    x=10
    def m1(self):
        print('Hello')
d=Details()
print(d.x)
d.m1()





name=input('enter the name: ')
age=int(input('enter the age: '))
location=input('enter the location: ')
class PersonalDetails:
    def display_details(self,name,age,location):
        print('Name is',name)
        print('Age is',age)
        print('Location is',location)
p=PersonalDetails()
p.display_details(name, age, location)





#Create a class named MathOperations.It should contain 4 methods to find out sum,difference,product and quotient.
#Each method has to take 2 parameter.Create an object for a class and call each method.Take input from keyboard
num1=int(input('enter the num1 value: '))
num2=int(input('enter the num2 value: '))
class MathOperation:
    def sum(self,num1,num2):
        print('The sum is',num1+num2)
    def sub(self,num1,num2):
        print('The difference is', num1-num2)
    def mul(self,num1,num2):
        print('The product is',num1*num2)
    def div(self,num1,num2):
        print('The quotient is',num1/num2)
m=MathOperation()
m.sum(num1,num2)
m.sub(num1,num2)
m.mul(num1,num2)
m.div(num1,num2)





z=30
class A:
    y=20
    def m1(self):
        x=10
        print(x)
        print(A.y)#using class name here y is printed, it's a cross variable
print(z)
a=A()
print(a.y)
a.m1()





#assume that your writing a python application for a training institute.
#Come up with at least 2 classes where each class will have 2 methods
class P_application:
    def course_details(self):
        course=input('enter the course: ')
        duration=4
        print(course,'course is confirmed')
        print('duration is',duration,'months')
    def fees(self):
        fees=4999
        print(fees,'/- fees')
class Stu_details:
    def student(self):
        name=input('enter the name: ')
        age=int(input('enter the age: '))
        print(name,age)
    def address(self):
        college=input('enter the college name: ')
        print(college)
p=P_application()
s=Stu_details()
p.course_details()
p.fees()
s.student()
s.address()




#__init__(self): is a spl method available for every class amd called whenever we created an object
class Details:
    def __init__(self): # passing parameters like (self,x,y)
        print('Hello') # if to print x and y values add print(x) and print(y)
    def m1(self):
        print('Bye')
d=Details()# then add here (x,y) values 
d.m1()





#Create a class Info with a constructor that take 3 parameters id,name,course and print them.
#Create 3 separate instances of that class
class Info:
    def __init__(self,id,name,course):
        print('Id:',id)
        print('Name:',name)
        print('Course:',course)

# 3 separate instances
i=Info(244,'Sana','python')
i=Info(204,'Sachin','python')
i=Info(454,'Sonu','python')




# using instance variable
class Info:
    def __init__(self,id,name,course):
        self.id=id  # instance variable
        self.name=name
        self.course=course
    def m1(self):
        print(self.id)
        print(self.name)
        print(self.course)
i=Info(1,'Sana','python')
i.m1()
j=Info(2,'Sinchu','java')
j.m1()
k=Info(3,'Anu','Data science')
k.m1()




#Create a class named Mathoperation with a constructor that takes 2 number as parameters.
#Create separate methods for addition, subtraction,multiplication and division which print the results.CAll those methods
class Mathoperation:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def addition(self):
        print('sum is',self.x+self.y)
    def subtraction(self):
        print('difference is',self.x-self.y)
    def multiplication(self):
        print('product is',self.x*self.y)
    def division(self):
        print('quotient is',self.x/self.y)
m=Mathoperation(32,18)
m.addition()
m.subtraction()
m.multiplication()
m.division()




# take a student class with 2 methods.init method should take 3 parameters no , name , sub.
# init method should print no , name , sub.
# display method should take 3 parameters no , name , sub.
# display method should print no , name , sub
# note: you have to call above 2 methods
class Student:
    def __init__(self,no,name,sub):
        print('no =', no)
        print('name =', name)
        print('sub =', sub)
        print('\n')
    def display(self,no,name,sub):
        print('no =',no)
        print('name =',name)
        print('sub =',sub)
s=Student(21,'sana','python')
s.display(22,'sachin','java')

print('\n')

# same question using constructor
class Student:
    def __init__(self,no,name,sub):
        self.no=no
        self.name=name
        self.sub=sub
    def display(self):

        print('no =', self.no)
        print('name =', self.name)
        print('sub =', self.sub)
s=Student(21,'sana','python')
s.display()



# create a student class with init and display methods.
# init method should have 3 parameters no,name,sub to initialize student object with values.
# display method should display student details. now create 3student objects with below values.
# also display each student details with corresponding objects
class Student:
    def __init__(self,no,name,sub):
        self.no=no
        self.name=name
        self.sub=sub
    def display(self):

        print('no =', self.no)
        print('name =', self.name)
        print('sub =', self.sub)
s1=Student(1,'Sana','python')
s2=Student(2,'Anu','Java')
s3=Student(3,'Sinchu','C++')
s1.display()
s2.display()
s3.display()



#sample
z=40
class Info:
    y=30
    print(z)
    def m1(self):
        # can we use this here to print the x  print(Info.y)
        self.y=20
        print(self.y)
i=Info()
i.m1()
print(Info.y)




class TypesMethods:
    def __init__(self):
        print('init method')
    def instance(self):
        print('instance method')

    @classmethod
    def class_method(cls):
        print('class method')

    @staticmethod
    def static_method():
        print('static method')
t=TypesMethods()
t.instance()
TypesMethods.class_method()
TypesMethods.static_method()




class Assignment:
    x = 10
    y = 20

    def method_one(self, x):
        self.z = 30
        print(Assignment.x)
        print(Assignment.y)
        print(self.z)


    @classmethod
    def method_two(cls, y):
        print(Assignment.y)
        print(Assignment.x)
        print(y)

a = Assignment()

a.method_one(50)
a.method_two(50)



class A: #parent class
    x=10

class B(A): #child class
    y=20

b=B()
print(b.y)
print(b.x)




# Types of inheritance
# single level inheritance
class A:
    x=10
class B(A):
    y=20
b=B()
print(b.x)
print(b.y)


print('\n')
# multilevel inheritance
class A:
    x=30
class B(A):
    y=40
class C(B):
    z=50
c=C()
print(c.x)
print(c.y)
print(c.z)

print('\n')
# hierarchical inheritance
class A:
    x=60
class B(A):
    y=70
class C(A):
    z=80
c=C()
print(c.x)
print(c.z)
b=B()
print(b.x)
print(b.y)


print('\n')
# multiple inheritance
class A:
    x=90
class B:
    y=100
class C(A,B):
    z=110
c=C()
print(c.x)
print(c.y)
print(c.z)



print('\n')
# hybrid inheritance
# combination of hierarchical and multiple
class A:
    w=120
class B(A):
    x=130
class C(A):
    y=140
class D(B,C):
    z=150
d=D()
print(d.w)
print(d.x)
print(d.y)
print(d.z)