def prime(n:int)->int:
    if(n==1):
        return 0
    k=int(n**0.5)+1
    for i in range(2,k):
        if(n%i==0):
            return 0
    return 1
a=int(input())
k=str(a)
if(prime(a) and prime(int(k[::-1]))):
    print("circular prime")
elif(prime(a)):
    print("prime but not a circular prime")
else:
    print("not prime")