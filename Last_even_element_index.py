n=int(input())
num=list(map(int, input().split()))
l=[]
for i in range(len(num)):
    if(num[i]%2==0):
        l.append(i)
print(l[-1])