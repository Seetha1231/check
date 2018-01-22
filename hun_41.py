def hun_41():
	n=int(input('Enter v :'))
	m=int(input('Enter e :'))
	l,ll,d,g,c=[],[],{},[],0
	for i in range(n):
		l.append(input('Enter vertex '+str(i)))
	for j in range(m):
		ll.append([input('Edge 1:'),input('Edge 2:')])
	for j in ll:
		if j[0] in d:
			d[j[0]].append(j[1])
		else :
			d[j[0]]=[j[1]]
	for i in d:
		for j in d :
			for k in d[i]:
				if k==j:
					c+=1
		d[i].append(c)
		c=0
	x=input('Enter vertex (has grandchild):')
	if x in d:
		if i[-1]==2:
			return 'Yes'
	return 'No'
  
hun_41()
