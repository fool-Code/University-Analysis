from black import Line
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import LineString

#Reading data
df = pd.read_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RL/data-rl-l.csv')
# Excluding the last row
'''
df2 = df.drop(df.index[-1:])
# Saving the altered dataframe
df2.to_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RL/data-rl-l.csv')
'''
ax = plt.gca()

df.plot(kind='line', x='f_hz', y='Vr',ax=ax)
df.plot(kind='line', x='f_hz', y='Vl',ax=ax)
df.plot(kind='line', x='f_hz', y='Vt',ax=ax)

# Finding the cutoff frequency
line_blue = LineString(np.column_stack(((df['f_hz'], df['Vr']))))
line_orange = LineString(np.column_stack(((df['f_hz'],df['Vl']))))
intersection = line_blue.intersection(line_orange)
# Plotting the cutoff frequency
plt.plot(*intersection.xy, 'ro')
# Showing the point coordinates
intersection_points = np.round(list(intersection.coords), decimals=3)
intersection_x = intersection_points[:,0]
intersection_y = intersection_points[:,1]
# Creating dotted lines
plt.axhline(intersection.y, xmax= 0.15, linestyle= 'dotted')
plt.axvline(intersection.x, ymax= 0.655, linestyle= 'dotted')
# Labeling the intersection
plt.text (intersection.x, intersection.y, '{},{}'.format(intersection_x, intersection_y))

#Plot legend
plt.legend(['Vr','Vl','Vt','Intersection'])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Tension(Volts)')
plt.title('RL Circuit Tensions')
plt.show()

