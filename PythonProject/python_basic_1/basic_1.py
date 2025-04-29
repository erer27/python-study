'''



딕트형:키와 값 => JSON
{"키":값,"키",값...}
=> 키는 중복이 불가능

집합데이터형 : list(set,tuple)
            set(list,tuple)
            tuple(list,set)
            --------------
            Collection
                |
        -------------------
        |       |       |
        List    Set     Map
        ----    ---     ---
                셀형      딕트형
        list(일차배열)
3) 제어문
    1. 조건문
        = 단일 조건문
          if 조건문: = 조건이 True일 때 처리
            문장
        = 선택 조건문
            if 조건문 : 
                처리문장 => 조건이 True일 때 처리되는 문장
            else:
                처리문장 => 조건이 false일 때 처리되는 문장
        = 다중 조건문
            => 조건에 맞는 조건문 1개 수행
            if 조건문:
                처리문장 => 조건이 True일 때 처리 => 종료
                    | False일 때
            elif 조건문:
                처리문장 => 조건이 True일 때 처리 => 종료
                    | False일 때
            elif 조건문:
                처리문장 => 해당 조건이 없는 경우
                            생략이 가능
            else:
                처리문장 => 해당 조건이 없는 경우
                           생략이 가능
        *** 들여쓰기 => yaml,yml
        *** switch는 없다
    2. 반복문
        while : 반복횟수가 없는 경우
                무한루프 while(True)
        형식)
            초기값
            while (조건):
                반복 처리 문장
                증감식 => 복합대입연산자 사용
                i++ (X) i=i+1 i+=1


        for : 반복횟수가 있는 경우
            for 받는변수 in range():
                반복 수행문장

            => range(1,10) => 1~9 : 마지막 제외
            => range(5) => 5바퀴
            => range(1,10,2) for(int i=1;i<10;i+=2)
                          -- 2씩 증가
            -------------------- 일반 for
            for-each
            for 받는 변수 in (list,set,tuple)
                처리 변수
    3. 반복제어문
        break : 반복의 종료
        continue : 특정부분을 제외
'''
# i=1
# while i<=10:
#     #print("i="+str(i))
#     #print(f"i={i}")
#     print("i=%d" %i)
#     i+=1
# for i in range(1,10): #9
#     print(f"i={i}")
# print("---------")
# for i in range(1,10,2): #9
#     print(f"i={i}")
# for i in range(5): #4
#     print(f"i={i}")
# print("-----------------")
# a=["홍길동","심청이","강감찬","이순신","박문수","홍길동","심청이"]
# for name in a:
#     print(name)
# b=("홍길동","심청이","강감찬","이순신","박문수","홍길동","심청이")
# print("-----------------")
# for name in b:
#     print(name)
# print("-----------------")
# # 순서가 없다, 데이터 중복이 없다
# c={"홍길동","심청이","강감찬","이순신","박문수","홍길동","심청이"}
# for name in c:
#     print(name)
d={"name":"홍길동","age":25,"sex":"남자"}
print(d['name'])
print(d['age'])
print(d['sex'])
# 데이터베이스 => 브라우저에 전송
print(d)