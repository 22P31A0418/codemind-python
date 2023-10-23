s=input()
count=0
for i in s:
    if(i>='A' and i<='Z'):
        count+=1
if(s[0]>='a' and s[0]<='z'):
    count+=1
print(count)