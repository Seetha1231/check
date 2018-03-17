def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    i,j=0,0
    while(i<n and j<n):
        if a[i]==b[j]:
            i+=1
            j+=1
        else :
            i+=1
            if i==3:
                break
    print(i-j)
if __name__ == '__main__':
    main()
