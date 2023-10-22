n=int(input())
num=list(map(int, input().split()))
a,b=map(int, input().split())
s=0
for i in range(len(num)):
    if(num[i]>=a and num[i]<=b):
        continue
    s=s+num[i]
print(s)