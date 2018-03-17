def main():
    s1,s2=map(str,input().split())
    try:
        mul=int(s1)*int(s2)
        print(str(mul))
    except:
        print('Invalid number string')



if __name__ == '__main__':
    main()
