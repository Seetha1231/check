def ifcop(n):
	flag=0
	for i in range(2,int(n/2)+1):
		if n%i ==0:
			return 0
	return 1
def coprime():
	n=int(input())
	m=int(input())
	f1=ifcop(m)
	f2=ifcop(n)
	if f1==1 and f2==1 :
		print('Yes')
	else :
		print('No')
try:
	coprime()
except:
	print('Invalid')
