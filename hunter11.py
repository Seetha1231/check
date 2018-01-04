def rever():
	s=input()
	l=list(s.split())
	r=[]
	s=''
	print(l)
	for i in range(len(l)):
		s+=l[i][::-1]+' '
	print(s)
try:
	rever()
except:
	print('invalid')
