n=int(input())
lst=list(map(int, input().split()))
ls=[i for i in lst]
lst.sort()
for i in range(0,len(ls)):
    print(lst.index(ls[i]),end=" ")
    