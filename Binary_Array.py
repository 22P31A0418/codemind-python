n=int(input())
num=list(map(int, input().split()))
for i in num:
    if(i!=0 and i!=1):
        print("False")
        break
else:
    print("True")