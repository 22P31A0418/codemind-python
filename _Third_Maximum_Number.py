n=int(input())
num=list(map(int, input().split()))
num=list(set(num))
num.sort()
if(len(num)<3):
    print(max(num))
else:
    print(num[-3])