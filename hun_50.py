def main():
    divident,divisor=list(map(int,input().split()))
    i=0
    while(divident>=divisor):
        divident-=divisor
        i+=1
    print(i)



if __name__ == '__main__':
    main()
