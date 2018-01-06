 def longpalindrome(st):
	n=len(st)
	table=[[0 for x in range(n)] for y in range(n)]
	i=0
	maxlen=0
	while(i<n):
		table[i][i]=True
		i=i+1
	start=0
	i=0
	while i<n-1:
		if st[i]==st[i+1]:
			table[i][i+1]=True
			start=i
			maxlen=2
		i=i+1
	k=3
	while(k<=n):
		i=0
		while(i<n-k+1):
			j=i+k-1
			if table[i+1][j-1] and st[i]==st[j]:
				table[i][j]=True
			if k>maxlen:
				start=i
				maxlen=k
			i=i+1
		k=k+1
	return st[0:maxlen+1]
try:
	longpalindrome('aabbbbba')
except:
	print('Invalid')
