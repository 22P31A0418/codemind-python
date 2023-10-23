n=int(input())
num=list(map(int, input().split()))
a,b=map(int, input().split())
max=0
c=0
for i in range(len(num)):
    if(num[i]>=a and num[i]<=b):
        continue
    if(num[i]>max):
        max=num[i]
        c=1
if(c==1):
    print(max)
else:
    print("-1")