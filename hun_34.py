def hun_34():
	s=input()
	ss=s
	f=0
	for i in range(0,len(s)-1):
		if int(ss[i])<int(ss[i+1]):
			d=list(ss)
			d[i+1],d[i]=d[i],d[i+1]
			ss="".join(d)
		if int(ss)>int(s):
			print(ss)
			f=1
			break
	if f!=1:
		print('Impossible')
try:
	hun_34()
except:
	print('Invalid')
