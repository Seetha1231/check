def swap():
	s=input()
	l=s.split()
	s=''
	for i in range(1,-1,-1):
		s+=l[i]+' '
	print(s)
try:
	swap()
except:
	print('invalid')
