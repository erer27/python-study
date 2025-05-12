import numpy as np

print(np.arange(10))
print(np.arange(5,10))
print(np.zeros((2,2))) #0으로 채운다 =>  행렬 => float
print(np.full((2,3),5))
# 나중에 값을 채워서 사용 np.array([[0,0,0],[0,0,0]])

a=np.arange(20)
print(a)
b=a.reshape((4,5))
print(b)

#Numpy 슬라이싱(자르기) / 인덱싱
lst=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
arr=np.array(lst)
a=arr[0:2,0:2]
print(a)
# python_numpy => 연산처리를 위한 라이브러리
# 1. 배열간 연산 기능 => + / - / / *
a=[1,2,3]
b=[4,5,6]
print(a+b) # list는 배열을 통합
c=np.array(a)
d=np.array(b)
print(c+d)
e=np.add(c,d)
print(e)
e=c+d
print(e)
e=c*d
print(e)
# * => multiply
e=c/d # 1/4 =0.25 , 2/5 0.4 , 3/6 0.5
print(e)
# / => divide
# 행렬 => dot() => 행렬의 곱
"""
    [[1,2]],  [[5,6],
    [3,4]]    [7,8]]
    
    1*5 + 2*7   , 1*6+2*8
    3*5 + 4*8   , 3*6+4*8
    
    수학 계산 = 행렬
"""
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
c=np.array(a)
d=np.array(b)
print(np.dot(c,d))

# 모든 배열 값의 합 sum(),  곱 prod()
a=np.array([[-1,2,3],[3,4,8]])
s=np.sum(a)
print(s)
p=np.prod(a)
print(p)
# 평균 / 표준 편차 / 표준 편차 std
# => 19/6
m=np.mean(a)
print(m)
ss=np.std(a)
print(ss)
"""
    10  8   10  8   8   4
    sum : 48 
    mean : 48/6 => 8 
    분산
        10  8 10  8  8  4
        -8 -8 -8 -8 -8 -8
        ------------------
        2   0  2  0  0  4
        ------------------
        2^2 2^2         4^2
          4  4           16 ===> 24
        24 / n-1 => 24/5 => 4.8

    표준편차
        4.8 루트 => 2.6.....
        
"""
