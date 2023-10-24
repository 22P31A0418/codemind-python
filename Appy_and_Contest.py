t=int(input())
for i in range(1,t+1):
    n,a,b,k=map(int, input().split())
    ap=n/(a*b)
    u=n/a+n/b-ap
    if(u>=k):
        print("Win")
    else:
        print("Lose")