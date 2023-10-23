n=int(input())
num=list(map(int, input().split()))
s=0
for i in range(0,n):
    s=s+num[i]
print(s)