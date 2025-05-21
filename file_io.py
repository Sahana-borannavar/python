'''
f=open('Sample.txt','w') # to create a text file
f.write('This is file operation') # to write a text in a created file
f.close() # to close a file

# once u closed the file we cant write anything in the file.
# we have to open again the file and add the new content.
# The old content written will be erased and new content will.
f=open('Sample.txt','a') # a - append method
f.write('I am learning python')
f.close()

f=open('Sample.txt','a') # a - append method
f.write('\nI am staying in Bng' ) # using \n will be displayed in new line/nxt line
f.close()


f=open('Sample.txt','r') # r - read method
res= f.read() # read(),readline() print only one line,readlines() print 1+ lines and reads the content in the list form
print(res)

print('\n')

f=open('Sample.txt','r')
res= f.readline()
print(res)

print('\n')
f=open('Sample.txt','r')
res= f.readlines()
print(res)

print('\n')




#create a file named info.txt
f=open('Info.txt','w')
f.write('Hello Good Morning')
f.write('\nHow was ur day going on')
f.close()
f=open('Info.txt','a')
f.write('\nThe day is going on well ')
f.write('\nHaving an enjoyment ')
f.close()

f=open('Info.txt','r')
res= f.read()
content=res.replace('Hello Good Morning','I have changed')
f.close()
f=open('Info.txt','w')
f.write(content)
f.close()
'''


# create a txt file Example.txt.
f=open('Example.txt','w')
f.write('This is file operation')
f.write('\nWe are crating a file')
f.close()
f=open('Example.txt','r')
res=f.read()
print(res)
print('\n')
content=res.replace('This is file operation','This is file I/O operation')
f=open('Example.txt','w')
f.write(content)
print(content)
f.close()