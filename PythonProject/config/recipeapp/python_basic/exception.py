'''
    예외처리 : 에러를 방지하고 정상 종료를 수행 (비정상 종료 방지)
    형식)
        try:
            정상수행문장
        except 예외처리종류:
            예외처리
        finally:
            무조건 수행문장 => 생략이 가능

    1. 파이선에서 제공하는 예외처리
            BaseException (Throwable)
                    |
            ------------------------------
            |                           |
           (Error)                     (Exception)
           => 수정이 불가능               => 에러 수정이 가능
           SystemExit                           |
           keyboardInterrupt                ArithmeticError
                                                = FloatingPointError
                                                = OverflowError
                                                = ZeroDivisionError
'''
# def display():
#     print(1)
#     print(2)
#     try:
#         print(3)
#         print(4)
#         print(10/0)
#         print(5)
#     except Exception as e:
#         print("6에러 발생:",e)
#     finally: # 무조건 (try,except상관없이 수행 = 서버닫기 , 데이터베이스 닫기
#         print(7)
#     print(8)
# display()
'''
    def list(page){
        try:
            page=request.GET['page']
        :except Exception as e:
            page="1"
'''
def div(a,b):
    return a/b

try:
    c=div(5,2)
    print(c)
    #c=div(5,0)
    print(c)

    e=[2,3]
    print(e[0])
    print(e[1])
    print(e[3])

    f=open('c:/pydata/upload.txt')
except Exception as e:
    print("에러메세지",e)
except ZeroDivisionError as e:
    print("에러메세지:",e)
except IndexError as e:
    print("에러메세지:",e)
finally:
    print("무조건 수행")
