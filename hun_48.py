 def hun_48():
	s=input()
	sub=input()
	n=len(sub)
	for i in range(len(s)-n+1):
		ss=''
		for j in range(i,len(sub)+i):
			ss+=s[j]
		if ss==sub:
			return i
	return -1
hun_48()
