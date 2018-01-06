 def hun_17():
	n=int(input())
	l,s,r=[],0,[]
	for i in range(n):
		for j in range(2):
			r.append(int(input()))
		l.append(r)
		r=[]
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i][1]==l[j][0] and l[i][0]==1:
				print(l[i][0],l[j][1])
				break
try:
	hun_17()
except:
	print('Invalid')
