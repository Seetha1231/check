def hun_22():
	n=int(input())
	l,s,out=[],0,[]
	for i in range(n):
		l.append(int(input()))
		out.append(1)
	for i in range(n):
		for j in range(n):
			if l[i]!=l[j]:
				out[i]*=l[j]
	print(*(out))
try:
	hun_22()
except:
	print('Invalid')
