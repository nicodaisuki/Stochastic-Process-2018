import numpy as np
import matplotlib.pyplot as plt
import math
sim=1000
T=10.0
pos=[0]
temp=[]
step=0.01
result=0
check=True
for i in range(sim):
	temp=np.random.normal(0,0.1,T/step)
	for j in range(1,(int)(T/step)):
		pos.append(temp[j-1]+pos[j-1])

	for k in range((int)(T/step)):
		if(pos[j]>2 and check):
			result=result+1
			check=False

	check=True
	pos=[0]
result=result/1000.0


print("By theory, P(W(10)>2)=0.265")
print("By simulation, P(W(10)>2)=%f" %(result))

