def main():
    l=list(map(str,input().split(',')))
    n=len(l)
    max=-1
    for i in l:
        str1=i.split("#")
        name=str1[0]
        m1,m2,m3=int(str1[1]),int(str1[2]),int(str1[3])
        sum=m1+m2+m3
        if max<sum:
            max=sum
            nam=name
    print(nam)

if __name__ == '__main__':
    main()
