 def loops():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	for i in range(n):
		for j in range(i+1,n):
			for k in range(j+1,n):
				if l[i]+l[j]==l[k]:
					print(l[i],l[j],l[k])
try:
	loops()
except:
	print('invalid')
