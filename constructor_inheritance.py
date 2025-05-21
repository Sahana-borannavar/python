class A:
    def __init__(self):
        print('Hi')
class B(A):
    def __init__(self):
        print('Bye')
b=B()

print('\n')

class A:
    def __init__(self):
        print('Hi')
class B(A):
    def m1(self):
        print('Bye')
b=B()



# using super class we can print both parent class,variables and methods
class A:
    def __init__(self):
        print('Hi')
class B(A):
    def __init__(self):
        super().__init__()
        print('Bye')
b=B()



# 1. Implement a student grading system.Create a class Student with the following:
# -A constructor to initialize the student's name,roll number and marks in three subjects.
# -A method calculate_average() to calculate the average marks.
# -A method display_grade() to display the grade  based on the avg marks.
#   -A for average >=90
#   -B for average >=75 and <90
#   -C for average >=50 and <75
#   -E for average <50
class Student:
    def __init__(self,name,roll,marks1,marks2,marks3):
        self.name=name
        self.roll_num=roll
        self.marks=[marks1,marks2,marks3]
    def calculate_average(self):
        return sum(self.marks)/len(self.marks)

    def display_grade(self):
        average=self.calculate_average()
        if average>=90:
            print('A Grade')
        elif average>=75:
            print('B Grade')
        elif average>=50:
            print('C Grade')
        else:
            print('E Grade')
    print(f'name')
s1=Student('Sana',41,[50],[60],[70])
s2=Student('Anu',22,[40],[50],[60])
s1.display_grade()
s2.display_grade()
