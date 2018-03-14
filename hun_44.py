def find(n):
    l=[]
    for i in range(10000):
        l.append("")
    l[0]=""
    size,m=1,1
    while size<=n:
        for i in range(0,m):
            if size+i<=n:
                l[size+i]="3"+l[size-m+i]
        for i in range(0,m):
            if size+m+i<=n:
                l[size+m+i]="4"+l[size-m+i]
        m=m*2
        size+=m
    print(l[n])
def main():
    n=int(input('Enter n :'))
    find(n)
if __name__ == '__main__':
    main()
