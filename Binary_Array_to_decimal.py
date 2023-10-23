n=int(input())
num=list(map(int, input().split()))
c=0
s=0
for i in range(-1,-n-1,-1):
    s+=num[i]*(2**c)
    c+=1
print(s)