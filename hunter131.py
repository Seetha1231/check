def altsort():
	n=int(input())
	l,r=[],[]
	for i in range(n):
		l.append(int(input()))
	c=0
	for i in range(n):
		m=l[i]
		p=i
		if c==0:
			for j in range(i+1,n):
				if m<l[j] :
					p=j
					m=l[j]
			l[i],l[p]=l[p],l[i]
			c=1
			continue
		if c==1:
			for j in range(i+1,n):
				if m>l[j]:
					p=j
					m=l[j]
			l[i],l[p]=l[p],l[i]
			l[i]=m
			c=0
	print(l)
