for _ in range(int(input())):
    a=int(input())
    s=0
    c=0
    while a:
        k=a%10
        s=s+(k*8**c)
        c+=1
        a=a//10
    print(bin(s)[2:])