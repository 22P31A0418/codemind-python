a,b,c=map(int, input().split())
if(a<=b and a<=c):
    l=b+c
elif(b<=a and b<=c):
    l=a+c
else:
    l=a+b
print(l)