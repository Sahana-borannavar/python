'''
'#calendar-display
import calendar
year=int(input('Enter the year: '))
month=int(input('Enter the month: '))
display=calendar.month(year,month)
print(display)


#datetime display
import datetime
print(datetime.datetime.now())

#math display
import math
print(math.factorial(5))
'''

'''
#area of triangle
base=float(input('enter the base : '))
height=float(input('enter the height: '))
triangle=(1/2)*base*height
print('The area of triangle is',triangle)
'''

'''
#conversion of miles into km
miles=float(input('enter the number of miles: '))
convert=1.6
kilometer= miles*convert
print(miles,'miles is equal to km',kilometer)
'''


'''
#swap 2 variables using a third variable
x=int(input('enter the first variable: '))
y=int(input('enetr the second variable: '))
print('original values:','x:',x,'y:',y)
temp=x
x=y
y=temp
print('swapped values: ','x:',x,'y:',y)
'''

'''
#conversion of celcius to farenheit
celcius=float(input('enter the value of celcius: '))
farenheit=(celcius*(9/5)+32)
print('the coversion of celcius into farenheit is ',farenheit )
'''

'''
#check weather the num is +ve , _ve or zero
num=float(input('enter the number: '))
if num>0:
    print('positive')
elif num==0:
    print('zero')
else:
    print('negative')
'''

'''
#multiplication table
num=int(input('enter the number of table to be displayed: '))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")
'''

