a=int(input())
if(a<=199):
    c=1.20
    b=a*c
elif(a>=200 and a<400):
    c=1.40
    b=a*c
elif(a>=400 and a<600):
    c=1.60
    b=a*c
elif(a>=600 and a<800):
    c=1.80
    b=a*c
elif(a>=800):
    c=2.00
    b=a*c
if(b>400):
    sc=0.15*b
else:
    sc=0
t=sc+b
print(f"Units Consumed: {a}")
print(f"Cost per Unit: {c:.2f}")
print(f"Bill: {b:.2f}")
print(f"Surcharge: {sc:.2f}")
print(f"Total Amount: {t:.2f}")