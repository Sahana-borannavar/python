'''
num1=int(input('enter the first number: '))
num2=int(input('enter the second number: '))
if num1>num2:
    print(f'the bigger number is {num1}')
else:
    print(f'the bigger number is {num2}')
'''

'''
num=int(input('enter the first number: '))
if num%2==0:
    print(num,' is even')
else:
    print(num,' is odd')
'''

'''
num1=int(input('enter the first number: '))
num2=int(input('enter the second number: '))
num3=int(input('enter the third number: '))
if num1>=num2 and num1>=num3:
    print(f'the biggest number is {num1}')
elif num2>=num1 :
    print(f'the biggest number is {num2}')
else:
    print(f'the biggest number is {num3}')
'''

'''
cha = input('enter the letter: ').lower()
if cha == 'a' or cha=='e' or cha=='i' or cha=='o' or cha=='u':
    print(cha, 'is a vowel')
else:
    print(cha, 'is a consonant')
'''

'''
year=int(input('enter the year: '))
if (year%400==0) or (year%4==0) and (year%100 !=0):
    print(year,'is a leap year')
else:
    print(year,'is not a leap year')
'''

'''
st=input('enter the string: ')
if st[::-1].lower()==st[::-1].lower():
    print(st, 'is a pallindrome')
else:
    print(st,'is not a pallindrome')
'''

'''
length=int(input('enter the length: '))
breadth=int(input('enter the breadth: '))
if length==breadth:
    print('it is a square')
else:
    print('it is a rectangle')
'''

'''
gender=input('enter the gender: ')
height=int(input('enter the height: '))
if gender=='male':
    if height>=188:
        print('he is eligible for admission')
    else:
        print('he is not eligible')
elif gender=='female':
    if height>=175:
        print('she is eligible for admission')
    else:
        print('she is not eligible')
else:
    print('not eligible')
'''
