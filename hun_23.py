def hun_23():
	n=int(input())
	k=int(input())
	l,s,r=[],0,[]
	for i in range(n):
		for j in range(k):
			r.append(int(input()))
		l.append(r)
		r=[]
	for i in range(n):
		for j in range(k):
			if l[i][j]!=0:
				s+=l[i][j]
	print(s)
try:
	hun_23()
except:
	print('Invalid')
