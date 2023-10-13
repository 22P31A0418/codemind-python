n=int(input())
num=list(map(int, input().split()))
s=0
k=0
for i in range(len(num)):
    if(i%2==0):
        s=s+num[i]
    else:
        k=k+num[i]
result=abs(s-k)
print(result)