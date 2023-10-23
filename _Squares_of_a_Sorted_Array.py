def square(n):
    return n*n
n=int(input())
num=list(map(int, input().split()))
num1=[square(i) for i in num]
num1.sort()
for i in num1:
    print(i,end=" ")