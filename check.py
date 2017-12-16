c=input()
l=['a','e','i','o','u','A','E','I',"O",'U']
if c.isnumeric() :
	print ('invalid character')
elif c in l:
	print ("vowel")
else :
	print ("consonant")
