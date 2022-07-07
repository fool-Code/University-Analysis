import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# data = {'D_10': pd.Series([29]),'D_25': pd.Series([33]),'D_35': pd.Series([34]), 'D_x':pd.Series([30])}
# df = pd.DataFrame(data)
df = pd.read_csv(r'C:\Users\c_hen\Desktop\Python\UEM\Refraction\data.csv')
nv = 1.57
h= 3.95
df['n_10'] = (nv * df['D_10'])/(np.sqrt((df['D_10']**2 + 16*(h**2))))
df['n_25'] = (nv * df['D_25'])/(np.sqrt(df['D_25']**2 + 16*(h**2)))
df['n_35'] = (nv * df['D_35'])/(np.sqrt(df['D_35']**2 + 16*(h**2)))
df['n_x'] = (nv * df['D_x'])/(np.sqrt(df['D_x']**2 + 16*(h**2))) 

df = pd.read_csv(r'C:\Users\c_hen\Desktop\Python\UEM\Refraction\cleandata.csv')
ax = plt.gca()
d_x = np.interp(14.2, df['D'],df['N'])
d_f = np.round(d_x, decimals=4)
df.plot(kind='line', x='D', y='N', ax=ax)
plt.text(14.2, d_x , '{},{}'.format(14.2, d_f))
plt.xlabel('Soluções (Porcentagem)')
plt.ylabel('Índice de Refração')

plt.show()