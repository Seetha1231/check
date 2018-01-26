 def hun_126():
	s=input()
	l=s.split()
	for i in l:
		if not i[0].isupper():
			return 'no'
	return 'yes'
hun_126()
