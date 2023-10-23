s=input()
t=input()
count=0
for i in s:
    if(i==t):
        count+=1
if(count==0):
    print(-1)
else:
    print(count)