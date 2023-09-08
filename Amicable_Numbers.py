m=int(input())
n=int(input())
k=0
h=0
for i in range(1,m):
    if(m%i==0):
        k=k+i
for i in range(1,n):
    if(n%i==0):
        h=h+i
if(k==n and h==m):
    print("Amicable")
else:
    print("Not Amicable")