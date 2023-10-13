n=int(input())
count=0
num=list(map(int, input().split()))
m=int(input())
for i in range(len(num)):
    if(num[i]==m):
        count=count+1
print(count)