# money=1000
# age=25
# if money>=500:
#     item="사과"
#     if age<30:
#         msg="new"
#     else:
#         msg="old"

'''
    반복문
    while / for
    while : 무한루프 = 지정된 횟수가 없는 경우
    for : 횟수가 지정된 경우
    
    while 형식
    초기화
    while 조건문 : 
        반복수행문장
        증가식
'''
# i=1
# while i<=10:
#     print("i=%d" %i)
#     i+=1 #i=i+1
# print("=============") # \n
# i=1
# while i<=10:
#     if i%2==0:
#         print("i=%d" %i)
#     i+=1
# print("===========")
#
# print("=============") # \n
# i=1
# while i<=10:
#     if i%2==1:
#         print("i=%d" %i)
#     i+=1
# print("===========")
#
# sum=0
# i=1
# while i<=100:
#     sum+=i
#     i+=1
# print(f"1~100까지 누적합:{sum}")
#
# evensum=0
# oddsum=0
# sum=0
# i=1
# while i<=100:
#     if i%2==1:
#         oddsum+=i
#     if i%2==0:
#         evensum+=i
#     sum+=i
#     i+=1
# print(f"{sum},{evensum},{oddsum}")
# print("==========================")
# #단을 입력받아서 구구단 출력
# i=1
# dan=int(input("단 입력:"))
# while i<=9:
#     print(f"{dan} * {i} = {dan*i}")
#     i+=1
'''
    for : 횟수가 지정된 경우 
    for 형식
        for 받는 변수 in 범위지정(리스트, 튜플)
                               -----  ---
                               List   Map
                                []     () => 데이터베이스
            범위지정 range(1,9)
            for(int i=1;i<10;i++)
            for i in range(1,10)
'''
# for i in range(1,10,2):
#     print(f"i={i}")
# print("=============")
# list=["red","blue","yellow","black","green"]
# for color in list:
#     print(color)
#
# for _ in range(5):
#     print("Hello")
# print("============")
# for i in range(1,10):
#     for j in range(2,10):
#         print(f"{j} * {i} = {i*j}",end="\t")
#     print(end="\n")

for i in range(1,5):
    for j in range(0,i):
        print("*",end="")
    print()

print("\n\n")

for i in range(4,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()