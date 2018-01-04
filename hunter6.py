 def repeat(l):
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i]==l[j]:
				return l[i]
	return 'Unique'
def main():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	print(repeat(l))
