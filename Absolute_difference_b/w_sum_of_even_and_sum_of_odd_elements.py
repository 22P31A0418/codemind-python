n=int(input())
x=list(map(int, input().split()))
s=0
k=0
for i in x:
    if(i%2==0):
        s=s+i
for i in x:
    if(i%2!=0):
        k=k+i
print(abs(s-k))