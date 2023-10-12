n=int(input())
num=list(map(int, input().split()))
k=sum(num)//(n)
print(k in num)