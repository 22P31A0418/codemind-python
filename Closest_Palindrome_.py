def pal(n:str)->int:
    k=n
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    return k==s
def prev_pal(n):
    while(n!=0):
        if(pal(n)):
            break
        else:
            n=n-1
    return n
def next_pal(n):
    while(n!=0):
        if(pal(n)):
            break
        else:
            n=n+1
    return n
n=int(input())
fn=prev_pal(n-1)
pn=next_pal(n+1)
if(n-fn==pn-n):
    print(fn,pn)
elif(n-fn>pn-n):
    print(pn)
else:
    print(fn)