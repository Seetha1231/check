def main():
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        min=l[i]
        for j in range(i):
            if l[i]>l[j]:
                min=l[j]
        print(min,end=" ")

if __name__ == '__main__':
    main()
