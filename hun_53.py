def main():
    st,nn=map(str,input().split())
    k=int(nn)
    s=""
    for i in range(len(st)):
        if k+i>len(st):
             break
        for j in range(i,k+i):
            s+=st[j]
        print(s,end=" ")
        s=""


if __name__ == '__main__':
    main()
