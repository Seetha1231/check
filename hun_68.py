def main():
    n=int(input())
    l=list(map(int,input().split()))
    max,min=-1,999
    for i in l:
        if max<i:
            max=i
        if min>i:
            min=i
    print(min,max)

if __name__ == '__main__':
    main()
