n=int(input())
num=list(map(int, input().split()))
c=0
for i in range(0,len(num)-2):
    if(num[i]%2==1 and num[i+2]%2==1 and num[i+1]%2==0):
        c+=1
print(c)