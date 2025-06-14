"""
    데이터 수집 : 크롤링 / 공공데이터 / 데이터셋
        | -- BS4, 셀레니움 ... CSV , 엑셀 , text , 오라클 ...
       분석
        |   -- Numpy / Pandas
       출력 (시각화) -- MatplotLib seaborn
       ---------------- 데이터 전처리
                            |
                           머신러닝 (학습)
                           딥러닝
                           ------------ AI
        Numpy : 배열 , 행렬 = 복잡한 여산 처리
          = 집합 데이터형
          리스트형 (list) => 배열 => []
          = 여러개의 값을 하나의 단위로 묶어주는 자료형 : 배열
          = 형식 [1,2,3,4,5]
          = 데이터 관리시 효율적으로 관리하기 위해 사용
                        ---------------
                         접근이 쉽고 수정이 가능
          = 인덱스로 처리 => 순서가 존재 , 중복 데이터 허용
            => ArrayList
          = 사용되는 위치 : 크롤링 데이터가 저장
          score=[100,200,[300,400,500],600]
                 0    1   -----------   3
                                2
          = JSON / CSV / XML
"""
"""
import numpy as np
a=[10,30,20]
b=[100,300,200]
c=a+b
print(c)
a1=np.array(a)
b1=np.array(b)
c1=a1+b1
print(c1)
"""
# score=[100,[200,300,400],500,600]
# # 인덱싱
# # [[[[[[[ ]]]]]]]
# # 2차원 배열 사용
# print(score[0])
# print(score[1][0])
# print(score[1][1])
# print(score[2])
# member=["홍길동",90,"박문수",90,"심청이",80,"이순신",100,"강감찬",75]
# print(member[0:2])
# print(member[2:])
# print(member[:])
#nums=[10,20,30,40,50,60,70,80,90]
# 요소 변경 / 추가 / 삭제
"""
    1. list => 크롤링  []
    2. tuple => 데이터베이스 ()
    3. dict => JSON {키:값}
    4. CSV => DataFrame => table(2차원)
              --------- MatplotLib
              ------------
               column...
              ------------
               value...
              ------------
               value...
              ------------ 
    5. 중복데이터 삭제 => set {}
"""

# nums=list(range(10))
# print(nums)
# #범위내 요소 변경
# nums[2:4]=[20,30]
# print(nums)
# nums[6:]=[60,70,80,90]
# print(nums)
# # 데이터 추가 => 맨뒤에 추가
# nums.append(50)
# print(nums)
# nums.append([100,200,300])
# print(nums)
# # 중간에 첨부
# nums.insert(0,1000)
# print(nums)
# nums=[10,20,30,40,50,60,70]
# #      0  1  2  3  4  5  6
# del nums[3]
# print(nums)
# del nums[3:]
# print(nums)
# # 전체 삭제 => nums[:] => clear
# nums.clear()
# print(nums)
# # 주요 함수
# score=[86,74,56,90,88]
# score.reverse()
# print(score)
# score.sort(reverse=True)
# print(score)
# # sort() / reverse(), del , append, insert , clear
# data=[1,2,3,1,4,5,6,3,2,1,6,7,9,8,8]
# print(set(data))
"""
    분석에 필요한 데이터형 : list,
"""
"""
    tuple
        :리스트와 비슷하지만 한번 값이 정해지면 변경이 불가능하다
        :데이터베이스 값 읽기
        :()
"""
# score=(90)
# print(score)
# score=(90,)
# print(score)
# score=10,20,30,40,50 #() 생략이 가능
# print(score)
# # 순서를 가지고 있다 => 인덱스번호가 만들어진다 => 0
# print(score[1:2])
# print(score)
# a=list(score)
# print(a)
# print(tuple(a))
"""
    set : 중복을 허용하지 않는다
            순서가 없는 자료형 (인덱스 번호가 없다) 
"""

def func(n):
    if n>=19:
        return True
    else:
        return False
ages=[30,45,20,18,38]
print("결과값:")
for a in filter(func,ages):
    print(a)
for a in filter(lambda x:x>=19,ages):
    print(a)
"""
    람다함수
    = 익명의 함수 
    = 간단한 기능 수행 , 빠르게 작성
    = 다른 함수의 매개변수를 전달할 때 사용
    = 복잡한 로직 / 여러줄 코드가 있는 경우에는 함수를 사용하는 것이 좋다
        => 재사용이 안된다
"""
# lambda 매개변수:표현식 (구현)
"""
    def 함수(매개변수)
        구현 
    
    map / reduce
    ---   ------
    count / 단어
    ------------ 하둡 (word count)
                 몽고디비 / ElasticSearch
                 ------    ------------
                 | NoSql => CRUD
"""
def add(x,y):
    return x+y
val=add(10,20)
print(val)

add=lambda x,y:x+y
print(type(add))
print(add(10,50))
print((lambda x:x+1)(5))

sum = lambda a,b:a*b
print(sum(10,20))
