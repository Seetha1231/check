def hun_43():
	s=input()
	l=list(s)
	p=[]
	k=0
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i].isdigit() and l[j].isdigit():
				a=l[i]+l[j]
				p.append(int(a))
				a=''
				break
	for i in l:
		if i.isalpha():
			print(i*p[k])
			if k<len(p):
				k+=1
