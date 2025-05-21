'''
# using append method
x= []
for i in range (0,102,2):
    x.append(i)
print(x)

# using range method
r=range(0,102,2)
li=list(r)
print(li)


#using for range method
x=[i for i in range(0,102,2)]
print(x)

# above all are known as list comprehension
'''


'''
#list comprehension
li=[1,5,6,8,3]

x=[li[i]**2 for i in range(len(li)) if i % 2 == 1]
#y=[]
#for i in range(len(li)):
#if i%2==0
#y.append(li[i]**2)

y=[li[i]*5 for i in range(len(li)) if i%2==0]
#x=[]
#for i in range(len(li)):
#if i%2==0
#x.append(li[i]*5)

z=[i*2 for i in li ]
#x=[]
#for i in li:
#x.append(li*2)

print(x)
print(y)
print(z)
'''


'''
# taking condition as multiple of three and not multiple of three
li=[11,3,6,10,13]
x=[i**2 for i in li if i%3==0]
print(x)

y=[i+5 for i in li]
print(y)

z=[i**2 for i in li if i%3!=0]
print(z)

print('\n')
#taking condition as less than 10 and greater than 10
li=[11,3,6,10,13]
x=[i**2 for i in li if i<10]
print(x)

y=[i+5 for i in li]
print(y)

z=[i**2 for i in li if i>10]
print(z)
# both are same but taking condition are different
'''

x=['hi','python','we','write','python','we','say','hi','python']
y={}
for i in x:
    if i in y.keys():
          y[i]=y[i]+1
    else:
        y[i]=1
print(y)


x = [ ('a',10),('b',20),('c',30),('d',40) ]
for i in x:
    print(i[1],end=' ')
print('\n')


x =['a', 'b', 'c', 'd']
y =[10, 20, 30, 40]
z={x[i]:y[i] for i in range(len(x))}
print(z)
print('\n')

x =['a', 'b', 'c', 'd']
y =[10, 20, 30, 40]
z=[(x[i],y[i]) for i in range(len(x))]
print(z)
print('\n')

'''
x = [('hi', 'noun'), ('good', 'adj'), ('run', 'verb'), ('bad', 'adj'), ('good', 'adj')]

good=0
bad=0

for word, pos in x:
    if word in count:
            [word] += 1
if good > bad:
    print('The sentiment is  positive')
elif bad > good:
    print('The sentiment is negative')
else:
    print('The sentiment is neutral ')
'''




