n=int(input())
num=list(map(int, input().split()))
a=0
b=0
for i in range(len(num)):
    if(num[i]%2!=0):
        a=a+1
        if(i%2!=0):
            b=b+1
if(a==b):
    print("True")
else:
    print("False")