# 문자열
# name = "홍길동"
# print(name)
import random

data="""
美, 관세 협상
조기 성과 의지…서두르지
않겠다는 韓과 온도차?"""
# print(data)
'''

'''
'''
b = True
c = False
print(b)
print(c)
'''

#입력
# print('이름 입력:')
# name = input()
# print(name,'님 반갑습니다')


# num = input("정수 입력:")
# print(f"num={num}")

'''
    파이썬 연산자
    1) 산술연산자
        +,-,*,/,%
        +
            문자열 + 문자열
            문자열 + 정수 (X)
            문자열 + 실수 (X)
            
            정수 / 정수 = 실수
            0으로 나눈 경우 : ZeroDivisionError (에러)
    2) 비교연산자
        == , !=, <,>,<=,>= => True/False
    3) 논리연산자
        and,or,not
        &&(X) , ||(X) , !(X)
    4) 대입연산자 
    5) 복합대입연산자
        += , -= , /= , %= , **=
        a=10
        a+=10 => a=a+10
    
    형변환 연산자 (X) => (int)10.5 int(10.5)
    증감연산자(X),삼항연산자(X)
                if ~else
    %
        나누는 값에 따라 부호 변경
    **
        10**2 => 100
'''
# a="Hello"
# b=10
# print(a+str(b)) # 정수는 문자열 변환후에 사용
# # str() = String.valueOf()

# a = 10
# b = 3
# print(a**b)
# print(not(a)) # ! => not()
# print(bool(a))

# print(5/2)
# print(5//2)

# 변수 = 반드시 초기화
a = random.randrange(10,101)
print(a)
while(True):
    user = input("정수 입력(1~100):")
    if user<a:
        print("입력값 보다 큰 값을 입력하세요")
    elif user>a:
        print("입력값 보다 작은값을 입력하세요")
    else:
        print("정답입니다")
        break

print("Game Over!!")

