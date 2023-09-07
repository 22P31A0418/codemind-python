n=int(input())
sum=0
pro=1
while(n!=0):
    i=n%10
    sum+=i
    pro*=i
    n=n//10
if(sum==pro):
    print("Spy Number")
else:
    print("Not Spy Number")