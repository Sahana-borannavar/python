# parameters in function
'''
def fun(name,bgrp,*disease,email='nothing'):
    print('name=' ,name)
    print('blood_grp=',bgrp)
    print('disease=',disease)
    print('email_id=',email)
fun('Bob','A+','cancer',email='bob@gmail.com')
fun('Jhon','AB-','Headache')
'''
'''
(or)
'''
'''
def fun(name,bgrp,*disease,email='not provided'):
    print(name)
    print(bgrp)
    for i in disease:
        print(i,end=' ')
    print('\n')
    print(email)
    print('\n')
fun('Bob','A+','cancer',email='bob@gmail.com')
fun('Jhon','AB-','Headache')

print('\n')
'''







def fun(name,*email,**address):
    print(name)
    for i in email:
        print(i)
    print('\n')
    for j in address:
        print(j,end=' ')

fun('Bob','bob@gmail.com','12bob@gmail.com','3rd cross','radhaswami colony',583232)
fun('Bob','bob@gmail.com','4th main road','attur layout',65713)











