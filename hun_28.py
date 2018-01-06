 def uniq():
	s=input()
	l=[]
	for i in range(len(s)):
		if s[i] not in l:
			l.append(s[i])
	print(*l)
try:
	uniq()
except:
	print('Invalid')
