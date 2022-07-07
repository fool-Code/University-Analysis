import pandas as pd

df = pd.read_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RC/data.csv')
df.drop(df.filter(regex='Unname'),axis=1, inplace=True)
df.to_csv('data-RC.csv', index=False)