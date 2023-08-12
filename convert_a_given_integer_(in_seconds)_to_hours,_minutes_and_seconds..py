n=int(input())
H=n//3600
M=(n%3600)//60
S=(n%3600)%60
print(f"H:M:S-{H}:{M}:{S}")