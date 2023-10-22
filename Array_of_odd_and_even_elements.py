n=int(input())
num=list(map(int, input().split()))
o=[]
e=[]
for i in num:
    if(i%2!=0):
        o.append(i)
    else:
        e.append(i)
print(*o,end=" ")
print(*e)