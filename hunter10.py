def subset():
	n=int(input())
	m=int(input())
	f=0
	a,b=[],[]
	for i in range(n):
		a.append(int(input()))
	for i in range(m):
		b.append(int(input()))
	for j in b:
		if j in a:
			continue
		else:
			f=1
			break
	if f==1:
		print('No')
	else :
		print('Yes')
