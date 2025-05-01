from django.db import models
import oracledb as db
import json
# 통계
# Create your models here.
'''
    파이썬:기본
            변수 / 연산자 / 제어문
            함수
            예외처리
            파일입출력
'''
def getConnection():
    try:
        conn=db.connect("hr/happy@localhost:1521/XE")
    except Exception as e:
        print(e)
    return conn
def disConnection(conn,cur):
    try:
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
def mainPageData():
    try:
        conn=getConnection()
        cur=conn.cursor()
        sql="""
                SELECT fno,name,poster,rownum 
                FROM (SELECT fno,name,poster
                FROM project_food ORDER BY fno ASC)
                WHERE rownum<=12
            """
        cur.execute(sql)
        food_list=cur.fetchall()
        cur.close()

        cur = conn.cursor()
        sql = """
                SELECT no,title,poster,rownum 
                FROM (SELECT no,title,poster
                FROM recipe ORDER BY no ASC)
                WHERE rownum<=12
                """
        cur.execute(sql)
        recipe_list = cur.fetchall()
    except Exception as e:
        print("errorrrrrrrrrrrr")
        print(e)
    finally:
        disConnection(conn,cur)

    return food_list,recipe_list


