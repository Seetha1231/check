def hun_15():
	n=int(input())
	l,s=[],0
	for i in range(n):
		l.append(int(input()))
	for i in l:
		s+=i
	print(s)
try:
	hun_15()
except:
	print("Invalid")
