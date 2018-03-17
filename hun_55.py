def main():
    n,d=map(int,input().split())
    l=list(map(int,input().split()))
    a=[]
    for i in range(d,n):
        a.append(l[i])
    for i in range(d):
        a.append(l[i])
    print(*a)

if __name__ == '__main__':
    main()
