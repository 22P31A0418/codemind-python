n=int(input())
for i in range(n):
    a=int(input())
    q=a
    s=0
    while(q!=0):
        r=q%10
        s=s*10+r
        q=q//10
    if(s==a):
        print("True")
    else:
        print("False")