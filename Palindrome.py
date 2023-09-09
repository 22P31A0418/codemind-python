def pal(n:str)->int:
    k=n
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    return k==s
n=int(input())
print(pal(n))