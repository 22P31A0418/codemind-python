n=int(input())
num=list(map(int, input().split()))
c=0
k=0
for i in range(0,n):
    if(num[i]%2==0):
        c+=1
    else:
        k+=1
print(c,k)