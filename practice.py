'''
n=int(input())
arr=list(map(int, input().split()))
arr.sort()
if n%2==1:
    print(arr[2])
else:
    print((arr[2]+arr[3])//2)



n=int(input())
arr=list(map(int, input().split()))
count={}
for movie_id in arr:
    count[movie_id]=count.get(movie_id,0)+1
for movie_id in sorted(count):
    print(movie_id,count[movie_id])
'''


n=int(input())
arr=list(map(int,input().split()))
arr=sorted()
print(set(arr))
