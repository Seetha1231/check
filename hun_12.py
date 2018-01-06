class stack:
	def __init__(self):
		self.a=[]
	def isEmpty(self):
		return len(self.a)==0
	def push(self,s):
		self.a.append(s)
	def pop(self):
		return self.a.pop()
 def hun_12():
	s=input()
	l=list(s)
	stack_obj=stack()
	f=0
	for i in range(len(s)):
		stack_obj.push(s[i])
	for i in range(len(s)):
		
		if l[i]==stack_obj.pop():
			continue
		else :
			f=1
			break
	if f!=1:
		print('Yes')
	else :
		print('No')
try:
	hun_12()
except:
	print('Invalid')
