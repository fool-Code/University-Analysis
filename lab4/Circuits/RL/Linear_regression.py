import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from shapely.geometry import LineString
import scipy.interpolate 
df = pd.read_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RL/data-rl-l.csv')

# Finding the inductance 
resistor = 218.9 # Omhs
df['X_l'] = (df['Vl']/df['Vr']) * resistor
plt.plot(df['f_hz'], df['X_l'])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Inductance')
plt.title('Reactance by Frequency')
plt.show()

# Performing linear regression
reg = LinearRegression()
# Split data
x = df[['f_hz']]
y = df[['X_l']]
# Modeling
reg.fit(x,y)
# Making prediction
y_pred = reg.predict(x)
# Printing the values
print(reg.coef_)
print(reg.intercept_)
plt.scatter(x,y)
plt.plot(df['f_hz'], y_pred)
plt.title('Linear Regression\n Inductance')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Inductance')
plt.show()

# Finding the impedance
resistor_square = resistor ** 2
df['Z'] = np.sqrt(((resistor_square) + (df[['X_l']] ** 2)))
# Plotting all the resistances 
df['R'] = resistor
ax = plt.gca()
df.plot(kind='line', x = 'f_hz', y = 'X_l', ax = ax)
df.plot(kind='line', x = 'f_hz', y = 'Z', ax = ax)
df.plot(kind ='line', x='f_hz', y = 'R', ax= ax)
plt.title('Resistances by Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Resistances (Omhs)')
# Finding the cutoff frequency 
line_blue = LineString(np.column_stack(((df['f_hz'], df['X_l']))))
line_orange = LineString(np.column_stack(((df['f_hz'], df['R']))))
intersection = line_blue.intersection(line_orange)
# Plotting the cutoff frequency
plt.plot(*intersection.xy, 'ro')
# Showing the point coordinates
intersection_points = np.round(list(intersection.coords), decimals=3)
intersection_x = intersection_points[:,0]
intersection_y = intersection_points[:,1]
# Creating dotted lines
plt.axhline(intersection.y, xmax= 0.15, linestyle= 'dotted')
plt.axvline(intersection.x, ymax= 0.12, linestyle= 'dotted')
# Labeling the intersection
plt.text (intersection.x, intersection.y, '{},{}'.format(intersection_x, intersection_y))
plt.show()

# Graph degree by Frequency
plt.plot(df['f_hz'], df['Degree'])
plt.title('Degree by Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Degree')

xdata = df['f_hz']
ydata = df['Degree']
x_inter = scipy.interpolate.interp1d(ydata,xdata)
print(x_inter(45))
x_cept = np.round(x_inter(45), decimals=3)
plt.text(x_cept,45, '{},{}'.format(x_cept, 45))
plt.show()
