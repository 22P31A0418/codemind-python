n=int(input())
num=list(map(int, input().split()))
se=int(input())
is_found = False
for i in num:
    if i==se:
        is_found = True
        break
print(is_found)