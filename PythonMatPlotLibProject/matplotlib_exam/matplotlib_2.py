import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df=sns.load_dataset("tips")
data=sns.get_dataset_names()
print(data)
url="https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2024"

# 반드시 <table>

# 1. hist plot
#sns.histplot(x=df['total_bill'])

p=sns.set_palette('BuGn')
#sns.histplot(x=df['total_bill'],palette=p)
# sns.histplot(x=df['total_bill'],y=df['tip'],palette=p)
# sns.boxplot(x=df['total_bill'],palette=p)
# sns.boxplot(y=df['total_bill'],x=df['smoker'],palette=p)
sns.lmplot(x='tip',y='total_bill',data=df,hue='sex',palette=p)
plt.show()
