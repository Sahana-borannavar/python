'''# first.py
import second
num = int(input("Enter a number: "))
second.even_odd(num)
'''
from calendar import firstweekday

'''
def m1():
    print('Hello')
def m3():
    print('Bye')
'''

li=[3,5,1,2,4]
def second_large(li):
    first=second=float('-inf')
    for num in li:
        if num>first:
            second=first
            first=num

        elif first > num > second:
            second=num
    return second if second!=float('-inf') else None
print(second_large(li))