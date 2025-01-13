import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats

"""
def calculate_mining_probability(p, T, x):

    a = math.e ** ((p - 1) / 10)

    luckywin = 2 - math.e ** (-p / 10 * (x - T)) + p * math.e ** (p*(T-x)/10)

    unluckywin = (
        2*math.e ** (T*p / 10) * p * (1 - p) * (math.e ** (-T/10) - math.e ** (-x/10))
    )
    prob = a**x / a**T * luckywin + unluckywin / a**T 
    return prob
"""

def cal_profit(q):
    return 2*q - 2*q*q + (2*q*q+q)*(2/(1+2*q)) ** (1/q)  
def cal_time(q):
    return -10/q*math.log(2/(1+2*q))



#pp=0.8 #input: portion of hashpower of the attacker

#print(pp, cal_time(pp), cal_profit(pp))


#Time wasted when applying postponing strategy per Block

def calculate_WastedTime(p, T):
    a = 2/(1+2*p)
    b = 1/p-1
    res = 10*b*math.e**(-T*p / 10)*(1+a*(math.log(a)-1)) - 10*a*b*math.e**(-T/10)*math.log(a)
    return res





xaxis = []  
yaxis = []
for pp in np.arange(0.85, 0.99, step=0.01):
    xaxis.append(pp)
    pro3 = 3*pp*(cal_profit(pp)-1)**2+2*pp*(cal_profit(pp)-1)-4*pp**2*(cal_profit(pp)-1)+3*pp+pp**3-2*pp**2
    pro2 = pp*cal_profit(pp)+pp*(1-pp)
    res3 = pro3/3/pp*30/(30+2*calculate_WastedTime(pp, 8))
    res2 = pro2/2/pp*20/(20+calculate_WastedTime(pp, 10))
    yaxis.append(res3)
print(np.argmax(yaxis)*0.01+0.85, max(yaxis))
plt.plot(xaxis, yaxis)
plt.show()  





"""
xaxis = []  
yaxis = []
for j in np.arange(0, 2, step=0.01):
    xaxis.append(j)
    profit = calculate_mining_probability(pp, 0, j)
    mixeds = 1  #in which probability is selfish hiding strategy played
    yaxis.append(profit)
print(pp, np.argmax(yaxis)*0.01, max(yaxis))
plt.plot(xaxis, yaxis)
plt.show()  

""" 
"""
fig, ax = plt.subplots()
ax.plot(xaxis, y2axis, label = 'honest mining')
ax.plot(xaxis, yaxis, label = 'hiding strategy')

plt.show()
"""



