n=int(input())
num=list(map(int, input().split()))
s=""
for i in num:
    s+=str(i)
s=int(s)+1
s=str(s)
for i in s:
    print(i,end=" ")