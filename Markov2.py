#Written by Kalvin Goode 9454554, 4/27/2018
import numpy as np
import matplotlib.pyplot as plt
import math
T=2
currT=0
state=2
spendT=[0,0]
jumpT=[]
for i in range(1000):
	while(currT<T):
		if(state==1):
			jumpT=np.random.exponential(0.3333333333,1)
			state=2
		elif(state==2):
			jumpT=np.random.exponential(0.5,1)
			state=1
		currT+=jumpT[0]
	if(state==1):
		spendT[0]+=1
		state=2
	else:
		spendT[1]+=1
	currT=0
print("By theory, the distribution is [0.6, 0.4].")
print("By simulation, the stationary distribution is [%f, %f]." %(spendT[0]/1000.0,spendT[1]/1000.0))
