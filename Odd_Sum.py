n=int(input())
s=0
num=list(map(int, input().split()))
for i in num:
    if(i%2!=0):
        s=s+i
print(s)