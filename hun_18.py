def hun_18():
	n=int(input())
	l,s,r=[],0,[]
	for i in range(n):
		for j in range(n):
			r.append(int(input()))
		l.append(r)
		r=[]
	for i in range(n):
		for j in range(n):
			if l[i][j]==1:
				s+=1
	print(s)
try:
	hun_18()
except:
	print('Invalid')
