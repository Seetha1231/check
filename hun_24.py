def hun_24():
	n=int(input())
	k=int(input())
	l,f=[],0
	for i in range(n):
		l.append(int(input()))
	for i in range(n):
		for j in range(i+1,n):
			if l[i]+l[j]==k:
				f=1
				break
	if f==1:
		print('Yes')
	else :
		print('No')
try:
	hun_24()
except:
	print('Invalid')
