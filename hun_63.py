def main():
    n=int(input())
    l=list(map(int,input().split()))
    max=-1
    for i in range(n):
        if i==n-1:
            l[i]=0
            break
        for j in range(i+1,n):
            if max<l[j]:
                max=l[j]
        l[i]=max
        max=-1
    print(*l)

if __name__ == '__main__':
    main()
