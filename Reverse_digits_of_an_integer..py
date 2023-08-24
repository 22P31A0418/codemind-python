n=int(input())
q=n
s=0
while(q!=0):
    b=q%10
    s=s*10+b
    q=q//10
print(s)