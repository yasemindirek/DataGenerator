import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

df = pd.read_csv("data.csv")
print(df.head())

# df.loc[(df['CorrectAnswer']<=100.0) & (df['AnswerTime']>=45.0), 'classes'] = 'basarisiz'  #en basarisiz
#
# df.loc[(df['CorrectAnswer']>=101) & (df['CorrectAnswer']<=200.0) & (df['AnswerTime']>=25) & (df['AnswerTime']<=40.0), 'classes'] = 'orta'  #orta
#
# df.loc[(df['CorrectAnswer']>=200) & (df['CorrectAnswer']<=300.0) & (df['AnswerTime']>=0) & (df['AnswerTime']<=20.0), 'classes'] = 'basarili'   #basarili

df.loc[(df['CorrectAnswer']<=100.0) , 'Degree'] = 'Unsuccessful'  #en basarisiz

df.loc[(df['CorrectAnswer']>=100) & (df['CorrectAnswer']<=200.0) , 'Degree'] = 'Average'  #orta

df.loc[(df['CorrectAnswer']>=200) & (df['CorrectAnswer']<=300.0) , 'Degree'] = 'Successful'   #basarili

df.to_csv("data.csv", index=False)

print(df.head(100))
