for _ in range(int(input())):
    n=int(input())
    s=1
    for i in range(2,n+1):
        if i%2==0:
            s=s^i
        else:
            s=s&i
    print(s)