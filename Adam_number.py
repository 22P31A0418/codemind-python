def rev(n)->int:
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
k=rev(n)
if(n**2==rev(k**2)):
    print("True")
else:
    print("False")