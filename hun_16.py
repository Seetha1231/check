 def hun_16():
	n=int(input())
	l,s=[],0
	for i in range(n):
		l.append(int(input()))
	k=int(input())
	for i in range(n):
		for j in range(n):
			if k==l[i]:
				print(l[i-2],l[i-1],l[i+1])
				break
try:
	hun_16()
except:
	print('Invalid')
