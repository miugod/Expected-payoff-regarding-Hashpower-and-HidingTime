import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats

#Expected payoff after applying hiding time strategy
def cal_profit(q):
    return 2*q - 2*q*q + (2*q*q+q)*(2/(1+2*q)) ** (1/q)

#best waiting time
def cal_time(q):
    return -10/q*math.log(2/(1+2*q))


#Time wasted when applying postponing strategy per Block
def calculate_WastedTime(p):
    res = 10*(1-p)/p*(2*p-1+2*math.log(2/(1+2*p)))/(1+2*p)
    return res



xaxis = []  
yaxis = []
for pp in np.arange(0.5, 0.99, step=0.01):
    xaxis.append(pp)
    res = cal_profit(pp)/(pp+1)/(1+calculate_WastedTime(pp)/10)
    yaxis.append(res)
print(np.argmax(yaxis)*0.01+0.5, max(yaxis))
plt.plot(xaxis, yaxis)
plt.show()  



