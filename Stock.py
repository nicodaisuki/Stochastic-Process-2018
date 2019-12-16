import numpy as np
import matplotlib.pyplot as plt
import math
W=[0]
S=[1.4]
record=0.0
rec=False
for i in range(1000):
	for j in range(250):
		temp=np.random.normal(0,0.1,1)
		W.append(W[j]+temp[0])
		S.append(1.4*math.exp(0.4*W[j+1]-0.4*0.4*(j/100)/2))
		if(S[j+1]>=2 and not rec):
			record=record+1
			rec=True
	rec=False
	W=[0]
	S=[1.4]

print ("By simulation, the fair price is %f." %(record/1000))


