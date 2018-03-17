def main():
    n=int(input())
    l=list(map(int,input().split()))
    f=0
    for i in range(n):
        for j in range(n):
            if l[i]==l[j]:
                f+=1

        if f==1:
            print(l[i])
        f=0
if __name__ == '__main__':
    main()
