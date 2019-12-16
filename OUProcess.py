import numpy as np
import matplotlib.pyplot as plt
import math
x=[-2]
record=[]
result=0
for i in range(1000):
	for j in range(100):
		x.append(x[j]-2*0.01*x[j]+3*(0.01)**(1/2)*np.random.normal(0,0.1,1))
	record.append(x[100])
	x=[-2]
result=sum(record)/1000.0
print ("By simulation, E(X(1))=%f." %(result))


