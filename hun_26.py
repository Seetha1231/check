 def hun_26():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	print(*l[::-1])
try:
	hun_26()
except:
	print('Invalid')
