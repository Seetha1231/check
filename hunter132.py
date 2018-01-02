def sumascii():
	s=input()
	sum=0
	for i in s:
		sum+=ord(i)
	print(sum)
try:
	sumascii()
except:
	print('invalid')
