 def ispalin(n):
	t=n
	r=0
	while(t!=0):
		r=r*10+t%10
		t//=10
	return(r==n)
def hun_40():
	d=int(input())
	s=0
	while(d!=0):
		s+=d%10
		d//=10
	print(ispalin(s))
try:
	hun_40()
except:
	print('Invalid')
