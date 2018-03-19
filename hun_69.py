def main():
    s=input()
    l=list(s)
    c=0
    for i in l:
        if i=='@':
            c+=1
        if i=='.':
            c+=1
    if c>2:
       # print('Error - @,. should present only one')
        return 'No'
    ba=s.split('@')
    a=ba[0]
    if len(a)<3:
        #print('Before @ there should be atleast 3 characters ')
        return 'No'
    a=ba[1]
    b=a.split('.')
    if len(b[0])<4:
       # print('Between @ and . there should be atleast 4 characters ')
        return 'No'
    if b[1]!='com':
        return 'No'
    return 'Yes'

if __name__ == '__main__':
    print(main())
