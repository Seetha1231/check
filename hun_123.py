def hun_123():
	s,ss=map(str,input().split())
	for i in range(len(s)-len(ss)+1):
		if s[i:len(ss)]==ss:
			return 'yes'
	return 'no'
hun_123()
