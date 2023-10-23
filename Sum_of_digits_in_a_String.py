s=input()
count=0
for i in s:
    if(i>='0' and i<="9"):
        count+=int(i)
print(count)