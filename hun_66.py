def main():
    n=input()
    l=list(map(str,input().split()))
    pre=str(input())
    c=0
    n1=len(pre)
    for i in l:
        s=i[0:n1]
        if s==pre:
            c+=1
    print(c)

if __name__ == '__main__':
    main()
