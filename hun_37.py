def hun_36():
	s=input()
	n=len(s)
	d=''
	if(n%2!=0):
		d+=s[n//2+1:]
		d=d[::-1]
		if(s[:n//2]==d):
			print('Yes')
			return
	print('No')
try:
	hun_36()
except:
	print('Invalid')
