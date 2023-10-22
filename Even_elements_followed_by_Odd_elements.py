n=int(input())
num=list(map(int, input().split()))
e=[]
o=[]
for i in num:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
print(*e,end=" ")
print(*o)