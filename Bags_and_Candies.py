n,a,b=map(int, input().split())
if(n%(a*b)==0):
    print(n//(a*b))
elif(n%(a*b)!=0):
    print((n//(a*b))+1)