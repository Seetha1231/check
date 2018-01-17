def hun_35():
	s=input()
	n=len(s)
	if(n%2!=0):
		if(s[:n//2]==s[n//2+1:]):
			print('Yes')
			return
	print('No')
try:
	hun_35()
except:
	print('Invalid')
