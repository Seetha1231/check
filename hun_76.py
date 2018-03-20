#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SEETHALAKSHMI
#
# Created:     26-02-2018
# Copyright:   (c) SEETHALAKSHMI 2018
# Licence:     <your licence>
#------------------------------------------------------------------------------)
def main():
    n=int(input())
    a=[ [0 for i in range(n)] for j in range(n) ]
    for i in range(n):
        l=list(map(int,input().split()))
        for j in range(n):
            a[i][j]=l[j]
    sum=0
    for i in range(n):
        for j in range(n):
            sum+=a[i][j]
    print(sum/(2*n))

if __name__ == '__main__':
    main()
