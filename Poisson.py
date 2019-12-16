import numpy as np
import matplotlib.pyplot as plt
import math
n=1000 # set n
time=0
jump=50
jumptimes=[[]]
currenttime=0
first=True
second=True
count=0
for i in range(n):
	s=np.random.exponential(0.5,jump)
	for j in range(jump):
		currenttime=currenttime+s[j]
		if(currenttime>1 and first):
			jumptimes[i].append(count)
			first=False
		elif(currenttime>2 and second):
			jumptimes[i].append(count)
			second=False
		count+=1
		jumptimes.append([])
	first=True
	second=True
	count=0
	currenttime=0
	
#calculating expect time
total=0
for i in range(n):
	total=total+jumptimes[i][0]*jumptimes[i][1]
expect=(float)(total)/n

print("By Calculation, E(N(1)N(2))=10, and by simulation, we have E(N(1)N(2))=", expect)
