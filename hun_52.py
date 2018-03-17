def findhop(n):
    if n==0 or n==1:
        return 1
    return findhop(n-1)+findhop(n-2)
def main():
    n=int(input())
    print(findhop(n))

if __name__ == '__main__':
    main()
