n,k,x,y=map(int, input().split())
r=n-k
s=k*x
if(x>=y):
    s=s+r*y
else:
    s=s+r*x
print(s)