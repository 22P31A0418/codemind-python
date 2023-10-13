n=int(input())
num=list(map(int, input().split()))
count=0
for i in range(0,len(num)-2):
    if(num[i]%2==0 and num[i+2]%2==1 or num[i]%2==1 and num[i+2]%2==0):
        count=count+1
print(count)
    