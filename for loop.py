# for loop

'''
li=[10,20,30,40,50]
for i in li:
    print(i,end=' ')
'''

'''
li=[10,20,30,40,50]
for i in range(len(li)-1,-1,-1):
    print(li[i],end=' ')
'''

'''
li=[10,20,30,40,50]
for i in range(0,5,2): #range(,0len(li),2)
    print(li[i],end=' ')
print(' ')

for i in range(3,0,-2): #range(len(li)-2,0,2)
    print(li[i],end=' ')
'''


'''
li=[10,20,13,61,50]
print('elements at even indices are: ')
for i in range(0,5,2):
    print(li[i],end=' ')
print(' ')

li=[10,20,13,61,50]
print('elements at odd indices are: ')
for i in range(1,5,2):
    print(li[i],end=' ')
print(' ')

for i in li:
    if i%2==0:
        print(i,'is an even number')
    else:
        print(i,'is an odd number')
print(' ')


sum=0
for i in li:
    sum=sum+i
print('sum of elements is',sum)
print(' ')

sum_even=0
sum_odd=0
for i in li:
    if i%2==0:
      sum_even=sum_even+i
    else:
        sum_odd=sum_odd+i
print('sum of even elements are', sum_even)
print('sum of odd numbers are',sum_odd)
print(' ')

sum=0
for i in range(0,5,2):
    sum=sum+li[i]
print('sum of even indices are',sum)
print(' ')

sum=0
for i in range(1,5,2):
    sum=sum+li[i]
print('sum of odd indices are',sum)
print(' ')
'''

'''
st=input('enter a string: ')
space_count=0
word_count=1
for i in st:
    if i ==' ':
        space_count= space_count+1
        word_count= word_count+ 1
print('number of space are ', space_count)
print('number of words are ', word_count)
'''


'''
ch=input('enter a character: ')
vowel='aeiouAEIOU'
for i in vowel:
    if ch==i:
        print(ch,'is a vowel')
        break
else:
    print(ch,'is not a vowel')

'''


li=[10,30,40,50,80]
biggest=0
for num in li:
    if num>=biggest:
        biggest=num
print(biggest)

li=[10,30,40,50,80]
smallest=80
for num in li:
    if num<=smallest :
        smallest=num
print(smallest)
