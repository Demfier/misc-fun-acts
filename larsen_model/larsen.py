import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

C_T = 0.78
D = 72.2  # diameter
R = D/2
A = math.pi * (R**2)
x = 2.5 * D

a1 = 0.435
a2 = 0.798
a3 = -0.125
a4 = 0.137
b1 = 15.63
I = 0.11
R_96 = a1 * ((b1 * I) + 1) * D * math.exp((a2 * (C_T**2)) + (a3*C_T) + a4)
m = 1/((1 - C_T)**0.5)
r0 = R * (((m+1)/2)**0.5)
x0 = (9.6*D)/(((R_96/r0)**3) - 1)
c1 = (r0**2.5) * math.pow(105/(2*math.pi), -0.5) * math.pow(C_T * A * x0, -5/6)

coordinates = 'ratio,r/d\n'  # output for the csv
ys = np.linspace(-2*D, 2*D, num=500)

for x in ys:
    try:
        p1 = math.pow(C_T * A * math.pow(x+x0, -2), 1/3)
        p2 = math.pow(y, 3/2)
        p3 = math.pow(3 * math.pow(c1, 2) * C_T * A * (x + x0), -0.5)
        p4 = math.pow(math.pow(35./(2*math.pi), 0.3) * (3 * math.pow(c1, 2)), -0.2)
        big_prod = math.pow(p2*p3 - p4, 2)
        ratio = 1 + ((p1 * big_prod)/9)
        coordinates += '{},{}\n'.format(ratio, y)
    except ValueError as e:
        continue


with open('larsen_points.csv', 'w') as f:
    f.write(coordinates)

df = pd.read_csv('larsen_points.csv')
sns.lmplot(x="r/d", y="ratio", data=df, fit_reg=False, scatter_kws={'marker': 'D', 's': 7})
plt.savefig('larsen_fig.png')
