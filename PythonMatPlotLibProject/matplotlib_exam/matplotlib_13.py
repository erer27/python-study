import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
"""
    df=pd.read_csv('c:/pydata/data_population.csv')
    print(type(df))
    print(df)
    
    "Province", 특별시 , 광역시 , 도
    "City", 구 군 시
    "Population", 인구수
    "Households" , 가구수
    "PersInHou", 평균 가족수
"""
df=pd.read_csv('c:/pydata/data_population.csv',encoding='cp949')
print(df)
f=open("c:/pydata/data_population.csv")
data=csv.reader(f)
next(data)
# 데이터에 저장
# result=[]
# for row in data:
#     if row[2]!=" ":
#         result.append(row[3])
# print(result)
# print(len(result))

city=input("지역 입력(시,도):")

seoul_pop=[]
seoul_city=[]

for row in data:
    if row[2]!=" ":
        if row[1]==city:
                seoul_pop.append(float(row[3]))
                seoul_city.append(str(row[2]))
plt.rc('font',family="Malgun Gothic")
plt.figure(figsize=(30,20))
plt.bar(seoul_city,seoul_pop)
plt.title(f"{city} 인구 통계")
plt.xticks(rotation=90)
plt.show()