n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
	v=i*l[i]
	if v in l:
		print(v)
		c+=1
print(c)
