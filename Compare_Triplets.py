ls1=list(map(int, input().split()))
ls2=list(map(int, input().split()))
o=0
l=0
for i in range(0,3,1):
    if(ls1[i]>ls2[i]):
        l=l+1
    elif(ls1[i]<ls2[i]):
        o=o+1
print(l,o)