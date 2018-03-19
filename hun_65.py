def main():
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    r=[]
    for i in l:
        if i!=k:
            r.append(i)
    l=r
    print(*r)

if __name__ == '__main__':
    main()
