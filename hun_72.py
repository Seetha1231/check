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
    l=list(map(str,input().split()))
    for i in range(0,len(l),2):
        s=l[i]
        l[i]=s[::-1]
    print(*l)



if __name__ == '__main__':
    main()
