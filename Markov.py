#Written by Kalvin Goode 9454554, 4/25/2018
import numpy as np
import matplotlib.pyplot as plt
import math
T=100
currT=0
state=1
spendT=[0,0,0]
jumpT=[]
while(currT<T):
	if(state==1):
		jumpT=np.random.exponential(0.3333333333,1)
		if(np.random.random()>0.6666666666):
			state=2
		else:
			state=3
		spendT[0]+=jumpT[0]
	elif(state==2):
		jumpT=np.random.exponential(0.2,1)
		if(np.random.random()>0.6):
			state=1
		else:
			state=3
		spendT[1]+=jumpT[0]
	elif(state==3):
		jumpT=np.random.exponential(0.2,1)
		state=1
		spendT[2]+=jumpT[0]

	currT+=jumpT[0]
print("By theory, the stationary distribution is [0.5814, 0.1163, 0.3023].")
print("By simulation, the stationary distribution is [%f, %f, %f]." %(spendT[0]/currT,spendT[1]/currT,spendT[2]/currT))
