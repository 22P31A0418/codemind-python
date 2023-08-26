m=int(input())
n=int(input())
for i in range(m,n+1):
    q=i
    count=0
    while(q!=0):
        r=q%10
        q=q//10
        if(r>0 and i%r==0):
            count+=1
    if(count==len(str(i))):
        print(i,end=' ')