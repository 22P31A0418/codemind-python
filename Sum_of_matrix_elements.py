n=int(input())
m=int(input())
num1=[]
for i in range(0,n):
    lst=list(map(int, input().split()))
    num1.append(lst)
s=0
for i in num1:
    s=s+sum(i)
print(s)