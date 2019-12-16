#Written by Kalvin Goode 9454554, 4/27/2018
import numpy as np
import matplotlib.pyplot as plt
import math
T=100
record=[0]
customer=[0]
server=[0]
time=0
state=-1
maxi=0
while(time<T):
	if(state==-1): #when no customer in line
		customer=np.random.exponential(0.5,1)
		time+=customer
		state+=1 #one more customer in line
		server=np.random.exponential(0.25,1) #serving time
		customer=np.random.exponential(0.5,1)  #next customer arrival time
	else:
		if(server[0]<customer[0]): #when serving is shorter than arrival
			for x in range(state+1):
				record[x]+=server[0]
			time+=server[0]
			customer[0]-=server[0]
			state-=1 #one less customer in line
			server=np.random.exponential(0.25,1) #serving time
		else: #when serving is longer than arrival
			time+=customer[0]
			for x in range(state+1):
				record[x]+=customer[0]
			server[0]-=customer[0]
			state+=1 #one more customer in line
			while(maxi<=state):
				record.append(0)
				maxi+=1
			customer=np.random.exponential(0.5,1) #next customer arrival time
print("By theory, the stationary distribution is [50, 25, 12.5 , 6.25, 3.125, 1.563, ...].")
print("By simulation, the distribution is [ ", end="")
for x in range(maxi-1):
	print(np.round(record[x],3),", ", end="")
print(np.round(record[maxi-1],3),"].")
