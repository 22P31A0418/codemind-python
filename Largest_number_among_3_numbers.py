a,b,c=map(int, input().split())
if(a<b and c<b):
    print(b)
elif(a<c and b<c):
    print(c)
else:
    print(a)