import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import LineString

# Reading data
df = pd.read_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RLC/data-rlc-I.csv')
# Excluding the last row
''' df2 = df.drop(df.index[-1:])
# Saving the altered dataframe
df2.to_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RLC/data-rlc-l.csv')
'''
# Plotting 
ax = plt.gca()

df.plot(kind='line', x='f_khz', y='Vr', ax=ax)
df.plot(kind='line', x='f_khz', y='Vl', ax=ax)
df.plot(kind='line', x='f_khz', y='Vc', ax=ax)
df.plot(kind='line', x='f_khz', y='Vt', ax=ax)

# Finding the point where Vr is equal to Vl
line_green = LineString(np.column_stack(((df['f_khz'], df['Vc']))))
line_orange = LineString(np.column_stack(((df['f_khz'], df['Vl']))))
intersection = line_green.intersection(line_orange)
# PLotting the intersection
plt.plot(*intersection.xy, 'ro')

# Showing the point coordinates
intersection_points = np.round(list(intersection.coords), decimals=3)
intersection_x = intersection_points[:,0]
intersection_y = intersection_points[:,1]
# Creating x and y lines
plt.text(intersection.x, intersection.y, '{},{}'.format(intersection_x,intersection_y))
plt.legend(['Vr','Vl','Vc','Vt','Intersection'])
plt.xlabel('Frequency (Khz)')
plt.ylabel('Tension (Volts)')
plt.title('RLC Circuit Tensions')
plt.show()


resistor = 98
resistor_sqr = 98**2
# Finding the inductance
df['X_l'] = (df['Vl']/df['Vr']) * resistor
# Finding the capacitance
df['X_c'] = (df['Vc']/df['Vr']) * resistor 
# Finding the current value 
df['I'] = (df['Vt']/np.sqrt(resistor_sqr + ((df['X_l']-df['X_c'])**2)))
# df.drop(df.filter(regex='Unname'),axis=1, inplace=True)
# df.to_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RLC/data-rlc-i.csv', index=False)
# df2 = pd.read_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RLC/rlc-group-i.csv', sep=';')
# df3 = pd.concat([df, df2], axis=1, sort=False)
# df3.drop(df.filter(regex='Unname'),axis=1, inplace=True)
# df3.to_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RLC/data-rlc-i-group.csv', index=False)

df2 = pd.read_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RLC/data-rlc-i-group.csv')
ax = plt.gca()
f0 = 34845
df2['f/f0'] = (df2['f_khz'] * 1000)/(f0) 
df2.plot(kind='scatter', x='f/f0', y='I', ax=ax)
df2.plot(kind='scatter', x='f/f0', y='I_n', ax=ax, color='red')
df2.plot(kind='scatter', x='f/f0', y='I_b', ax=ax, color='orange')
df2.plot(kind='scatter', x='f/f0', y='I_m', ax=ax, color='purple')
plt.legend(['I','I_n','I_b','I_m'])
plt.xlabel('Frequency by Resonant Frequency')
plt.ylabel('Currents (A)')
plt.title('RLC Circuit Currents')
plt.show()

