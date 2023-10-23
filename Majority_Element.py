n=int(input())
num=list(map(int, input().split()))
max=0
for i in range(0,n):
    c=0
    for j in range(0,n):
        if(i!=j):
            if(num[i]==num[j]):
                c=c+1
    if(c>max):
        max=c
        d=num[i]
print(d)