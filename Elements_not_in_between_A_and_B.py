n=int(input())
num=list(map(int, input().split()))
a,b=map(int, input().split())
c=0
for i in range(len(num)):
    if(num[i]>=a and num[i]<=b):
        continue
    else:
        c=1
        print(num[i],end=" ")
if(c==0):
    print("-1")