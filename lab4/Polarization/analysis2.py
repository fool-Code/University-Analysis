import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv(r'Polarization\exp2.csv')
# df.drop(df.filter(regex='Unname'),axis=1, inplace=True)

# Performing a experimental math
df['I_exp'] = ((np.cos((df['degree'])*(np.pi/180)))*(np.sin((df['degree'])*(np.pi/180))))**2
# df['I_exp'] = df['I_exp']*(180/np.pi)
i_res = 0.04
df['I_sub'] = df['current'] - i_res
ax = plt.gca()
df.plot(kind='line', x='degree', y='I_sub',ax=ax)
df.plot(kind='line', x='degree', y = 'I_exp', ax=ax)
plt.legend(['Experimental','Teórico'])

plt.xlabel('Ângulo (graus)')
plt.ylabel('Corrente (mA)')

plt.show()
