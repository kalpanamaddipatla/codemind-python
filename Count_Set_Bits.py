for _ in range(int(input())):
    n=int(input())
    k=bin(n)[2:]
    d=list(k)
    c=0
    for i in d:
        if i=='1':
            c+=1
    print(c)
            
    