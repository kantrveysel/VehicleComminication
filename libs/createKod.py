from itertools import combinations as com
from random import random

z = [2,3,5,7,11]

def carp(A):
	k=1
	if len(A)<0:
		return 0
	for i in A:
		k*=i
	return k
	
def create():
	ke=[]
	for i in com(z,3):
		carp(i)
		ke.append(str(carp(i))+"989"+"989".join([str(int(random()*100)) for i in range(3)]))
	return list(map(hex,map(int,ke)))