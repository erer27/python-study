'''
변수 설정:
 변수 = 값 (데이터형을 사용하지 않는다)
       반드시 초기화
 연산자
  = 형변환 연산
        정수 : int(문자열)
        실수 : float()
        문자열 : str()
        논리형 : bool()
  = 정수/정수=정수
        //
  = 제곱근
        **
  = 논리연산자
        && => and , || => or , ! => not
  = 증감연산자(++,--),삼항연산자 (X)

'''
# a=10 # int a=10
# # 복수의 주소에 저장
# b=c=d=10 # int a,b,c; a=b=c=10
# e,f=100,200 # int e=100, f=200

#산술연산자
# a=10
# b=3
# print(a+b) #13
# print(a-b) #7
# print(a*b) #30
# print(a/b) # 3.333333
# print(a//b) # 3
# print(a%b) # 1
#
# print(a**b) # 1000
#
# name1='홍'
# name2='길동'
# print(type(name1))
# print(type(name2))
# print('홍'+'길'+'동')
# print('홍길동'*10) # 10번 출력(반복)
# print('홍길동'+str(10))
# print(int("10")+10)
# print(10.5+float(10))
# print(bool(0),bool(-1),bool(0.0),bool(0.1))
# # 0, 0.0 제외
# print(bool('홍'),bool(''))
# #문자열은 공백을 제외한 모든 문자는 True
# # int(), float(), bool() , str()
# #비교연산자
# a=10
# b=9
# print(id(a),id(b))
# print(a==b)
# print(a is b) # 주소값 비교 (참조하는 주소)
# =>  조건문 / 반복문 => True/False
'''
        and / or
    -----------------------
        and(직렬)     or(병렬)
    -----------------------
    TT      T           F
    -----------------------
    FT      F           F
    -----------------------
    
        (조건) and(or)    (조건)
        ----              ------
          |                 |
          -------------------
                    |
                  결과값
        부정 연산자 : not() => True/False
                    0,0,0, 공백을 제외한 나머지 False
'''
# a = 10
# b = 20
# c = 0
# print(not(a<b))
# print(not(a))
# print(not(b))
# print(not(c))

x = 10
y = 9
print(x<y and x==y+1)
print(x>y and x==y+1)

x+=20 # x=x+1 x++ x+=1
y-=10 # y=y-10 x-- x-=1
print(x,y)



