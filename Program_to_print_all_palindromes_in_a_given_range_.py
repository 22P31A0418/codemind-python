def is_pal(n):
    k=n[::-1]
    if(n==k):
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(is_pal(str(i))):
        print(int(i),end=" ")