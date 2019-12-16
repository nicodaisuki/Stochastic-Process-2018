import numpy as np
import matplotlib.pyplot as plt
import math
n=100 # set n
claims=[]
for i in range(n):
	s=np.random.poisson(2*365)
	t=np.random.exponential(1/2.3,s)

	claims.append(np.sum(t))
claims=np.sort(claims)

print("By Calculation, The value at risk for confidence level 90% is 338.65 and by simulation, we have ",claims[90])
