n=int(input())
sum=0
pro=0
for i in range(1,n+1,1):
    sum+=(i*i)
    pro+=i
print(abs((pro*pro)-sum))