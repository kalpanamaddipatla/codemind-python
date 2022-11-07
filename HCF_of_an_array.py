n=int(input())
d=list(map(int,input().split()))
k=min(d)
c=0
for i in d:
    if i%k==0:
        c+=1
if c==n:
    print(k)
else:
    print('1')