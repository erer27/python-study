"""
    슬라이싱 / 인덱싱

"""
import numpy as np

a=np.array([1,2,3,4,5])
#인덱싱
b=a[0] #1
c=a[1] #2
for i in range(len(a)):
    print(a[i])
d=a[1:4] # 2 3 4
print(d)
e=a[:3] # 인덱스 0,1,2 => 123
f=a[3:] # 4,5
print(e,f)

arr=np.array([[1,2,3],[4,5,6]])
a=arr[0,0]
b=arr[1,2]
print(a,b)

c=np.concatenate((a,b)) #병합
print(c)
a=np.array([1,2,3,4,5,6])
b,c=np.split(a,[3]) #분리할 때 사용
print(b,c)