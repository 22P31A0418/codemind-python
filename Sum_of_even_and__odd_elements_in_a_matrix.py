r,c=map(int, input().split())
mat=[]
for i in range(r):
    inner_list=list(map(int, input().split()))
    mat.append(inner_list)
s=0
k=0
for inner_list in mat:
    for every_value in inner_list:
        if(every_value%2==0):
            s+=every_value
        else:
            k+=every_value
print(f"{s} {k}")