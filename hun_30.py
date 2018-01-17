def hun_30():
	c=0
	n=int(input())
	s=[int(input()) for i in range(n)]
	f=[int(input()) for i in range(n)]
	for i in range(n):
		if f[i]>s[i]:
			c+=1
	print(c)
try:
	hun_30()
except:
	print('Invalid')
