 def closez():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	for i in range(n):
		for j in range(i+1,n):
			if l[i]+l[j]==0 :
				print(l[i],l[j])
try:
	closez()
except:
	print('invalid')
