def hunt_12():
	n=int(input())
	k=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	l.sort(reverse=True)
	print(l[k-1])
try:
	hunt_12()
except:
	print("Invalid")
