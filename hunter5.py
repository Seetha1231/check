def f():
	s=input()
	d=''
	c=1
	r=[]
	for i in range(len(s)-1):
		v=int(s[i])
		if v<26:
			d=s[i]+s[i+1]
			if v>26:
				continue
			c=c+1
	print(c)
try:
	f()
except:
	print('invalid')
