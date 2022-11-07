n=int(input())
d=list(map(int,input().split()))
k=min(d)
m=[]
c=0
s=0
for i in range(1,k+1):
    if k%i==0:
        m.append(i)
for i in m:
    s=0
    for j in d:
        if j%i==0:
            s+=1
    if s==n:
        c=i
print(c)
        
