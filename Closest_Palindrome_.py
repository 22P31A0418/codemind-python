def paln(n):
    if(n==n[::-1]):
        return True
    else:
        return False
def prev_paln(n):
    while(n):
        if(paln(str(n))):
            return n
        n-=1
def next_paln(n):
    while(n):
        if(paln(str(n))):
            return n
        n+=1
n=int(input())
f=prev_paln(n-1)
l=next_paln(n+1)
if(n-f==l-n):
    print(f,l)
elif(n-f<l-f):
    print(f)
else:
    print(l)