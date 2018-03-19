def main():
    n=int(input())
    c=0
    l=[1000,500,100,50,10,1]
    for i in l:
        while(n>=i):
            if n-i>=0 :
                print(n,n-i)
                n=n-i
                c+=1
    print(c)
if __name__ == '__main__':
    main()
