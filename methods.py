from tkinter.font import names

from requests import delete

li=[10,20]
li.append([30,40])
print(li)

li=[10,20,30,40,50]
li.pop(4)
print(li)

li=[10,20,30,40,50]
li.remove(50)
print(li)

li=[10,20,30,40,50]
li.insert(1,100)
print(li)

li=[10,20,30,40,50]
li.extend([60,70,80])
print(li)


'''
#list methods
li=[]
for i in range(10):
    lis=int(input('enter the elements : '))
    li.append(lis)
print(li)
position=int(input('enter the position: '))
element=input('enter the new element: ')
if position>=0 and position<=len(li):
    li.insert(position,element)
print('new list',li)
de=int(input('enter the element to delt: '))
if de in li:
    li.remove(de)
    print('deleted list',li)
else:
    print('not found')
ele=int(input('enter the element: '))
position=li.index(ele)
if ele in li:
    print('element position: ',position)
else:
    print(-1)
    
'''

'''
#tuple methods
tu=(10,20,30,40,50)
ele=int(input('enter the elements: '))
if ele in tu:
    print('The index of element is:',tu.index(ele))
else:
    print(ele,'is not found in tuple')
'''

'''
#set methods
s=set()
for i in range(5):
     ele= int(input('enter the elements : '))
     s.add(ele)
print(s)
de=int(input('enter the element to delete: '))
if de in s:
    s.remove(de)
print('deleted set',s)
# here we can use direct index to find position instead we convert the set into list and then we find position list(s).index(pos
pos=int(input('enter the element to find position: '))
position= list(s).index(pos)
if pos in s:
    print('element position: ', position)
'''


#dictionary methods

name=input('enter the name: ')
email=input('enter the email: ')
mobile=input('enter the mobile: ')
city=input('enter the city: ')
pin=input('enter the pincode: ')
di={
    'name':name,
    'email':email,
    'mobile':mobile,
    'city':city,
    'pincode':pin
}
print('\nContents:')
for i,j in di.items():
    print(i,'=',j)
new_name=input('enter the new name: ')
di['name']=new_name
print('\ncontents')
for i,j in di.items():
    print(i,'=',j)
key=input('enter the key to remove: ')
if key in di:
    di.pop(key)
    print(key,'removed')
else:
    print(key,'not removed')
value=input('enter the value: ')
if value in di.values():
    print('value found')
else:
    print('value not found')
di['state'] = input('Enter state: ')

print('Updated Dictionary: ')
for i,j in di.items():
    print(i,'=',j)