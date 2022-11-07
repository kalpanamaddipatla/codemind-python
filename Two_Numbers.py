a=int(input())
d=list(map(int,input().split()))
k=[]
for i in d:
    if d.count(i)==1:
        k.append(i)
k=sorted(list((k)))
for i in k:
    print(i,end=" ")