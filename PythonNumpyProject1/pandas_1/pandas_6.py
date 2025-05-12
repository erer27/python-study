"""
    Numpy
        = 수치 계산을 위한 라이브러리
          --------
           배열 연산 (벡터)
           선형 대수
           통계 , 난수 생성 => 수학적 기능 제공
        = 대용량의 데이터 연산을 빠르게 수행할 수 있게
          최적화된 라이브러리
        = 다차원 배열 제공 (ndarray)
           ** 포함하면 안된다
        = 다른 라이브러리의 연동 : pandas , scikit-learn
        = pip install numpy
        = import numpy as np
        3. 난수
        randint() : 정수 추출
        rand() : 0~1사이의 실수
        4. 배열 연산
            +, -, *, /
            a=np.array([1,2,3])
            b=np.array([10,20,30])
            a+b => add(a,b) [11,22,33]
            a-b => substract(a,b) [9, 18, 27]
            a*b => multiple(a,b) [10,40,90]
            a/b = divide(a,b) [10,10,10]
        5. 확인
            행,열 => shape
            전체 개수 => size()
            인덱싱 / 슬라이싱
            a=np.array([1,2,3,4,5])
            a[2] => 3
            a[1:4] => 2 3 4

            a[2] => 3
            a[1:4] => 2 3 4
        
        6. 집계함수
            합:sum
                a.sum(axis=0) : 세로
                a.sum(axis=1) : 가로
                a.sum(axis=(0,1))
            평균 : mean()
            최대값 : max()
            최소값 : min()
"""
import numpy as np
import pandas as pd

# a=np.array([1,2,3,4,5])
# print(a)
# line=np.linspace(0,10,5)
# print(line)
# 특정 조건에 맞는 인덱스
arr=np.array([1,2,3,4,5])
index=np.where(arr>3)
print(arr[index])
"""
    Pandas : 데이터 분석 / 데이터 조작을 위한 라이브러리
     = 엑셀 , CSV , SQL , JSON
        데이터를 쉽게 처리가 가능하게 만든 라이브러리
        
        => Tuple = List로 변경
"""
data=[1,2,3,4,5]
series=pd.Series(data)
print(series)
# 기본적으로 숫자 인덱스(0)가 할당된다
# => 원하는 인덱스로 지정이 가능
data=[100,200,300]
index_lab=["a","b","c"]
series=pd.Series(data,index=index_lab)
print(series)
print(series["a"])