# 내장 데이터베이스가 존재 sqlite => 400만개
'''
    1. 함수 (사용자 정의)
        = 웹 연결 => URL을 읽어서 해당 함수를 호출
                    ----------
                
                    GateWay => MSA
    현재                |
                -------------------------
                |           |           |
             NodeJS    Spring-Boot     Django
               |            |           |
               ---------------------------
'''
'''
    함수 형식
    --------
    def 함수명(매개변수...):
        기능 처리
        return 값,값 => 없는 경우에는 사용하지 않는다 (void)
               ---- return값이 여러개인 경우도 있다 
    *** 파이썬은 기본 => 데이터형 사용하지 않는다
                       --------------------
                        => 가독성 (X)
    *** 수집 / 분석 / 통계 => 시각화 
    자바 => 웹
    C => 하드웨어
    C# => 웹 MS
'''
import pymysql as pm
#연결
def getConnection():
    conn=pm.connect(host="127.0.0.1",user="root",password="happy",db="mydb",charset="utf8")
    return conn
def disConnection(conn,cur):
    cur.close()
    conn.close()

# 전체 목록 읽기
def empListData():
    conn=getConnection()
    cur=conn.cursor()
    sql=("""SELECT empno, ename, sal, job,date_format(hiredate,'%Y-%m-%d'),
            dname,loc
            FROM emp JOIN dept
            ON emp.deptno=dept.deptno
        """)
    cur.execute(sql)
    emp_list=cur.fetchall()
    disConnection(conn,cur)
    return emp_list
# 검색
def empFindData(ename):
    conn=getConnection()
    cur=conn.cursor()
    sql=f"""
            SELECT * FROM emp
            WHERE ename LIKE concat('%','{ename}','%') 
        """
    cur.execute(sql)
    emp_list=cur.fetchall()
    cur.close()
    conn.close()
    return emp_list
# 상세보기
def empDetailData(empno):
    conn=getConnection()
    cur=conn.cursor()
    sql=f"""
            SELECT empno,ename,job,
            date_format(hiredate,'%Y-%m-%d'),sal
            FROM emp
            WHERE empno={empno}
        """
    cur.execute(sql)
    emp_data=cur.fetchone()
    cur.close()
    conn.close()
    return emp_data
# 추가 => dept => () Tuple형태로 전송
def deptInsert(dept):
    conn=getConnection()
    cur=conn.cursor()
    sql="""
            INSERT INTO dept 
            VALUES(%s,%s,%s)
        """
    cur.execute(sql,dept)
    conn.commit()
    print("데이터 추가 완료!!")
    disConnection(conn,cur)


def deptUpdate(dept):
    conn=getConnection()
    cur=conn.cursor()
    sql="""
        UPDATE dept SET
        dname=%s, loc=%s
        WHERE deptno=%s
        """
    cur.execute(sql,dept)
    conn.commit()
    disConnection(conn,cur)
def deptDelete(deptno):
    conn=getConnection()
    cur=conn.cursor()
    sql=f"""
            DELETE FROM dept
            WHERE deptno={deptno}
        """

    cur.execute(sql)
    conn.commit()
    print("데이터 삭제 완료")
    disConnection(conn,cur)
# 전체 기능 수행
def main():
    while(True):
        print("1.사원목록")
        print("2.사원검색")
        print("3.상세보기")
        print("4. 데이터추가")
        print("5. 데이터 삭제")
        print("6. 데이터 수정")
        print("7. 종료")
        menu=int(input("메뉴 선택:"))
        if menu==7:
            print("프로그램 종료")
            break
        elif menu==1:
            emp_list=empListData()
            for emp in emp_list:
                e=list(emp)
                print(e)
        elif menu==2:
            ename=input("이름 입력:")
            emp_list=empFindData(ename)
            for emp in emp_list:
                e=list(emp)
                print(e)
        elif menu==3:
            empno=int(input("사번 입력:"))
            emp_data=empDetailData(empno)
            print(f"사번:{emp_data[0]}")
            print(f"이름:{emp_data[1]}")
            print(f"직위:{emp_data[2]}")
            print(f"입사일:{emp_data[3]}")
            print(f"급여:{emp_data[4]}")
        elif menu==4:
            dept=(50,'영업부','부산')
            deptInsert(dept)
        elif menu==6:
            dept=('자재부','서울',50)
            deptUpdate(dept)
        elif menu==5:
            deptDelete(50)
"""
    list => 가장 많이 사용 => 일차원 배열
     => a=[1,2,3,4,5...]
        a[0], a[1]....
     tuple => 데이터베이스 값 
     => b=(1,2,3,4,5....)
        b[0],b[1]....
     => set => 중복을 허용하지 않는다 (제거 => 장르)
        c={1,2,3,4,...}
        c[0],c[1]
    -----------------------------------
     => dict => Map => JSON과 연결
        d={"a":1,"b":2...}
        d['a'] d['b']
    ----------------------------------- 웹으로 전송시에 주로 사용
    
"""


main()
