import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from shapely.geometry import LineString


df = pd.read_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RC/data2.csv')

df['f1'] = df['f_khz'] * 1000
df['Xc'] = (df['Vc'] / df['Vr']) * 98.89
plt.plot(df['f1'], df['Xc'])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Reactance')
plt.title('Reactance by Frequency')
plt.show()
df['f-1'] = (1/df['f1'])
plt.plot(df['f-1'], df['Xc'])
plt.title('Reactance by Inverse Frequency')
plt.xlabel('Frequency Inverse')
plt.ylabel('Reactance')
plt.show()
# Performing linear regression
reg = LinearRegression()
# Spliting data
x = df[['f-1']]
y = df[['Xc']]
# Have to model first
reg.fit(x,y)
# Making prediction
y_pred = reg.predict(x)

print(reg.coef_)
print(reg.intercept_)
plt.scatter(x,y)
plt.plot(df['f-1'], y_pred)
plt.title('Linear Regression\n Reactance')
plt.xlabel('Frquency Inverse')
plt.ylabel('Reactance')
plt.show()

# Finding the impedance
resistor = 98.69
resistor_square = resistor ** 2
df['Z'] = np.sqrt(((resistor_square) + (df[['Xc']] ** 2)))
# Plotting all the resistances 
df['R'] = resistor
ax = plt.gca()
df.plot(kind='line', x = 'f1', y = 'Xc', ax = ax)
df.plot(kind='line', x = 'f1', y = 'Z', ax = ax)
df.plot(kind ='line', x='f1', y = 'R', ax= ax)
plt.title('Resistances by Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Resistances (Ω)')
# Finding the cutoff frequency 
line_blue = LineString(np.column_stack(((df['f1'], df['Xc']))))
line_orange = LineString(np.column_stack(((df['f1'], df['R']))))
intersection = line_blue.intersection(line_orange)
# Plotting the cutoff frequency
plt.plot(*intersection.xy, 'ro')
# Showing the point coordinates
intersection_points = np.round(list(intersection.coords), decimals=3)
intersection_x = intersection_points[:,0]
intersection_y = intersection_points[:,1]
# Creating dotted lines
plt.axhline(intersection.y, xmax= 0.25, linestyle= 'dotted')
plt.axvline(intersection.x, ymax= 0.12, linestyle= 'dotted')
# Labeling the intersection
plt.text (intersection.x, intersection.y, '{},{}'.format(intersection_x, intersection_y))
plt.show()
