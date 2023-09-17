n=int(input())
count=1
lst=list(map(int,input().split()))
for i in lst:
    if i>=n:
        count=0
        break
if(count==1):
    print("YES")
else:
    print("NO")