n=int(input())
num=list(map(int, input().split()))
c=0
avg=sum(num)//len(num)
for i in num:
    if(i<=avg):
        c+=1
print(c)
