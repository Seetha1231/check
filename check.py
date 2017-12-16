c=input()
l=['a','e','i','o','u','A','E','I',"O",'U']
if int(c) :
	print ('Invalid character')
elif c in l:
	print ("vowel")
else :
	print ("consonant")
