n=int(input())
ls1=list(map(int, input().split()))
m=int(input())
ls2=list(map(int, input().split()))
targ=[]
for i in range(0,n):
    targ.insert(ls2[i],ls1[i])
for i in targ:
    print(i,end=" ")