n=int(input())
ls=list(map(int, input().split()))
c=0
i=0
m=0
while(i<n):
    if(ls[i]==1):
        c+=1
        if(c>m):
            m=c
    else:
        c=0
    i+=1
print(m)