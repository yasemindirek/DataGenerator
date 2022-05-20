import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())

df.loc[(df['CorrectAnswer']<=100.0) , 'Degree'] = 'Unsuccessful'  #en basarisiz

df.loc[(df['CorrectAnswer']>=100) & (df['CorrectAnswer']<=200.0) , 'Degree'] = 'Average'  #orta

df.loc[(df['CorrectAnswer']>=200) & (df['CorrectAnswer']<=300.0) , 'Degree'] = 'Successful'   #basarili

df.to_csv("data.csv", index=False)


