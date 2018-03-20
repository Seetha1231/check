def main():
    n,k,t=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(n):
        sum=l[i]
        for j in range(n):
            if l[j]!=l[i]:
                for c in range(j,j+k-1):
                    if c>=n:
                        break
                    sum+=l[c]
                if sum==t:
                    return "Yes"
                sum=l[i]
    return "No"
    
if __name__ == '__main__':
    print(main())
