'''
import numpy as np
# Create a NumPy array from a python list
arr=np.array([1,2,3,4,5])
print(arr)



# To create a multi-dimensional array (2*2)
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[1,2],[3,4]])
res1=np.matmul(arr1,arr2) #mathametical-multiplication
res2=arr1*arr2 # normal multiplication
print(res1)
print(res2)




#2*3 and 3*2 output will be 2*2
import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[1,2],[3,4],[5,6]])
res=np.matmul(arr1,arr2)
print(res)




# take 2*3 matrix and find its transpose
# transpose means rows become column and colum become rows
import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
res=np.transpose(arr1)
print(res)



# Find inverse
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
det=np.linalg.det(A)
if det==0:
    print('No inverse')
else:
    adjugate = np.array([[ A[1,1], -A[0,1]],
                     [-A[1,0],  A[0,0]]])
    res=(1/det)*adjugate
    print(res)



import numpy as np
# create an array with values from 0 to 9
arr=np.arange(10)
print(arr)



import numpy as np
arr=np.arange(12)
reshaped_arr=np.reshape(arr,(3,4))
print(reshaped_arr)



# finding mean
import numpy as np
arr=np.array([[1,2,3],
             [4,5,6]])
row_mean=np.mean(arr,axis=1)
col_mean=np.mean(arr,axis=0)
print(row_mean)
print(col_mean)



import numpy as np
arr=np.array([[1,2,3],
              [4,5,6]])
col_sum=np.sum(arr,axis=1)
#col_sum=np.sum(arr,axis=0)
print(col_sum)



# print random numbers
import numpy as np
rand_arr=np.random.rand(5)
print(rand_arr)
'''