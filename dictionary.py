'''
di={
    'x':10,
    'y':20
}
for i,j in di.items():
    print(i,'=',j)

di={
    'x':10,
    'y':20
}
for i in di.keys():
    print(i)

di={
    'x':10,
    'y':20
}
for i in di.items():
    print(i)
'''


'''
house_num=int(input('enter the house number: '))
street=input('enter the street: ')
city=input('enter the city: ')
pincode=int(input('enter the pincode: '))
di={
    'house num': house_num,
    'street': street,
    'city': city,
    'pincode': pincode
}

for i,j in di.items():
    print(i,'=',j)
'''

'''
# print 5 elements
li =[ ]
for i in range(5):
    num=int(input('enter the elements: '))
    li.append(num)
print(li)
'''

'''
num=int(input('enter a number: '))
original=num
rev=0

while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
if original==rev:
    print(original,'is a palindrome')
else:
    print(original,'is not a palindrome')
'''

'''
# prime number
num=int(input('enter a number: '))
i=2
prime=True
if num>1:
    while i<num:
        if num%i==0:
            prime=False
            break
        i+=1
    if prime:
        print(num,'is a prime number')
    else:
        print(num,'is not a prime number')
else:
    print(num,'is not a prime number')
'''