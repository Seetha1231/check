def main():
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    ll=[]
    for i in range(n):
        for j in range(n):
            dif=l[i]-l[j]
            if dif == k:
                c+=1
    print(c)
if __name__ == '__main__':
    main()
