n=int(input())
max=0
ls=list(map(int, input().split()))
for i in ls:
    if(ls.count(i)==1):
        if(i>max):
            max=i
if(max==0):
    print(-1)
else:
    print(max)