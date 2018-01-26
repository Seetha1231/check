def hun_128():
	st=input()
	n=len(st)
	table=[[0 for i in range(n)] for j in range(n)]
	max=1
	i=0
	while(i<n-1):
		table[i][i]=True
		i+=1
	start=0
	i=0
	while(i<n-1):
		if st[i]==st[i+1]:
			max=2
			start=i
			table[i][i+1]=True
			print(st[start:start+max])
		i+=1
	k=3
	while(k<=n):
		i=0
		while(i<(n-k+1)):
			j=i+k-1
			if table[i+1][j-1]==True and st[i]==st[j]:
				table[i][j]=True
				if max<k:
					max=k
					start=i
					print(st[start:start+max])
			i+=1
		k+=1
	print(st[start:start+max])
hun_128()
