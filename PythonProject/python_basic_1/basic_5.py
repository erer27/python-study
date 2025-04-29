'''
    MySQL => CRUD (SELECT, INSERT, UPDATE, DELETE)
    => SQL문장은 ANSI (표준화) 데이터형 / 함수 
'''

#SELECT
import pymysql as pm
from oracledb import connect
conn=pm.connect(host="localhost",user="root",password="happy",db="mydb",charset="utf8")
#PreparedStatement => 송수신 => SQL전송 , 실행결과값 읽기
cur=conn.cursor()
# SQL실행
# sql=f"""
#         SELECT hakbun,name,kor,eng,math,
#         ROUND((kor+eng+math)/3.0,2) as age ,
#         (kor+eng+math) as total
#         FROM student
#     """
# cur.execute(sql)
# #실행결과값 읽기 = Tuple () : 변경이 불가능
# std_tuple=cur.fetchall()
# # 닫기
#
# # 화면에 출력
# for std in std_tuple:
#     s=list(std)
#     print(s)
# '''
#
# '''
# # fetchall(selectList) fetchone(selectOne)
# #oracle.connect("hr/happy@localhost:1521/xe")
# # mysql / mariadb => 3306
# #           => AWS (docker)
# #INSERT
# name=input("이름 입력:")
# kor=int(input("국어 점수:"))
# eng=int(input("영어 점수:"))
# math=int(input("수학 점수:"))
# sql=f"""
#     INSERT INTO student(name,kor,eng,math)
#     VALUES(%s,%s,%s,%s)
#     """
# data=(name,kor,eng,math)
# cur.execute(sql,data)
# conn.commit()
# cur.close()
# conn.close()
# print("저장 완료")

# item=[
#     ('이산',90,80,70),
#     ('춘향이',70,90,90),
#     ('을지문덕',80,80,60)
# ]
# sql="""
#     INSERT INTO student(name,kor,eng,math)
#     VALUES(%s,%s,%s,%s)
#     """
# for row in item:
#     cur.execute(sql,row)
# #commit 전송
# conn.commit()
# print("데이터 첨부 완료")
# # 닫기
# cur.close()
# conn.close()
hakbun=int(input("삭제할 학번 입력"))
sql=f"DELETE FROM student WHERE hakbun={hakbun}"
cur.execute(sql)
conn.commit()
cur.close()
conn.close()
print("삭제 완료")
#UPDATE
# SQL문장 => Oracle과 동일 (데이터형,함수)
#DELETE
#함수화
#객체 지향 (class) 
#파일 입출력 / 예외처리
#Numpy, Pandas , MatplotLib(Seaborn)
#분석 : KoNlp , 웹 Django
#ElasticSearch : 검색엔진 AWS
#Spring - Boot / React => 32일
