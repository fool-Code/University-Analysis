import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import LineString

# Reading data
df = pd.read_csv(r"C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RC/data.csv")
# Removing spaces from columns headers 
# df.columns = df.columns.str.replace(' ', '')
# Saving file or rather overwriting 
# df.to_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RC/data.csv')
# Excluding the last row
df2 = df
# df2.to_csv(r'C:/Users/c_hen/Desktop/Python/UEM/Lab4/Circuito-RC/data2.csv')
# Creating a line plot with all voltages
ax = plt.gca()

df2.plot(kind='line', x='f_khz', y='Vt',ax=ax)
df2.plot(kind='line', x='f_khz', y='Vr',ax=ax)
df2.plot(kind='line', x='f_khz', y='Vc',ax=ax)
# Finding the point where Vr is equal to Vc
line_blue = LineString(np.column_stack(((df2['f_khz'], df2['Vr']))))
line_orange = LineString(np.column_stack(((df2['f_khz'], df2['Vc']))))
intersection = line_blue.intersection(line_orange)
# Plot the intersection
plt.plot(*intersection.xy, 'ro')

# Showing the point coodinates
intersection_points = np.round(list(intersection.coords), decimals=3)
intersection_x = intersection_points[:,0]
intersection_y = intersection_points[:,1]
# Creating x and y lines
plt.axhline(intersection.y, xmax = 0.27 , linestyle = 'dotted')
plt.axvline(intersection.x, ymax= 0.65, linestyle = 'dotted')
# labeling the intersection
plt.text(intersection.x, intersection.y, '{},{}'.format(intersection_x, intersection_y))

# Showing plot legend
plt.legend(['Vt','Vr','Vc','Intersection'])
plt.xlabel('Frequency (Khz)')
plt.ylabel('Tension (Volts)')
plt.title('RC Circuit Tensions')
plt.show()

# Graph degree by frequency 
plt.plot(df['f_khz'],df['Degree'], color='Red')
plt.title('RC Circuit \n Degree by Frequency')
plt.xlabel('Frequency (khz)')
plt.ylabel('Degree')
plt.show()