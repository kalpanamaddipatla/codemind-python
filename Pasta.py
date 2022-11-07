a,b=map(int,input().split())
d=list(map(int,input().split()))
k=list(map(int,input().split()))
c=0
for i in k:
    if i in d:
        c+=1
        d.remove(i)
if c==b:
    print('Yes')
else:
    print('No')
    