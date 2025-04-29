import pymysql as pm
import oracledb as db
# java => import java.sql.*
# join 
#1. connection 객체 생성
conn=pm.connect(host="localhost",
                user="root",password="happy",
                db="mydb",charset="utf8")
# conn=DriverManager.getConnection(url,"","")
#2. PreparedStatement 생성
cur=conn.cursor()
# ps=conn.preparedStatement()
#3. SQL문장 전송 => 실행
# sql=f"""
#         SELECT empno,ename,job,date_format(hiredate,'%Y-%m-%d') as regdate,
#         sal,dname,loc
#         FROM emp JOIN dept
#         ON emp.deptno=dept.deptno
#     """
# cur.execute(sql)
# # execute, executemany(여러개를 동시에 추가)
# #4. 결과값 얻기
# emp_join=cur.fetchall()
# #5. 함수 = return
# #6. cursor/connection 닫기
# cur.close()
# conn.close()
# #7. 데이터 출력
# print(emp_join)
# for row in emp_join:
#     data=list(row)
#     print(data)

#8. 데이터프레임 변경
#9. 시각화
#10. 이미지화 => 스프링의 realpath
# subquery
'''
    1. SQL
        DQL : SELECT = 데이터 검색
                SELECT *|column_list...
                FROM 테이블|View|(SELECT~)
                [
                    WHERE 조건
                    GROUP BY 그룹컬럼
                    HAVING 그룹 조건
                    ORDER BY 컬럼명 (ASC|DESC)
                ]
        DML : 데이터 조작언어
                INSERT = 데이터 추가
                INSERT INTO table_name(컬럼1,컬럼2...)
                VALUES(값1,값2..)
                
                UPDATE = 데이터 수정
                DELETE = 데이터 삭제
        DCL : 데이터 제어언어
              GRANT = 권한 부여
              GRANT CREATE VIEW TO 계정
              REVOKE = 권한 해제
              REVOKE CREATE VIEW FROM 계정
        DDL : 정의 언어 
              CREATE / DROP / ALTER / RENAME / TRUNCATE
        TCL : 일괄처리
              COMMIT / ROLLBACK 
        기타 : JOIN / SubQuery / View 만들기
                                = 보안 , 쿼리문장이 복잡한 경우
                    = 스칼라 서브쿼리 , 인라인 뷰
            = innter join / outer join (left,right)
'''
# like
# findData=input("이름 입력:")
# conn=pm.connect(host="127.0.0.1",user="root",
#                 password="happy",db="mydb",charset="utf8")
# cur=conn.cursor()
# sql=f"""
#     SELECT empno,ename,job,date_format(hiredate,'%Y-%m-%d') as hiredate
#         ,sal,dname,loc
#         FROM emp,dept
#         WHERE emp.deptno=dept.deptno
#         AND ename LIKE concat('%','{findData}','%')
#     """
# cur.execute(sql)
# data=cur.fetchall()
# cur.close()
# conn.close()
#
# print(data)
# sql="""
#     SELECT empno,ename,job,hiredate,sal,
#     (SELECT dname FROM dept WHERE deptno=emp.deptno) as dname,
#     (SELECT loc FROM dept WHERE deptno=emp.deptno) as loc
#     FROM emp
#     """
# cur.execute(sql)
# data=cur.fetchall()
# cur.close()
# conn.close()
# print(data)
# param=(7788)
# # cur.execute("SELECT * FROM emp WHERE empno=%d" %param)
# conn=db.connect("hr/happy@localhost:1521/xe")
# cur=conn.cursor()
# cur.execute("SELECT * FROM emp WHERE empno=:empno",{"empno":7788})
#
# data=cur.fetchall()
# cur.close()
# conn.close()
# print(data)
sql="""
    UPDATE student SET
    name=%s, kor=%s, eng=%s, math=%s
    WHERE hakbun=%s
    """
param=('홍길동 수정',90,90,90,1)
cur.execute(sql,param)
conn.commit()
print("수정 완료")
