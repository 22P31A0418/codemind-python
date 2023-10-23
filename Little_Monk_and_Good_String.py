s=input()
count=0
mx=0
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
    else:
        count=0
    mx=max(mx,count)
print(mx)