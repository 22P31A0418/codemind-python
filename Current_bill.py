u=int(input())
if(u<199):
    uc=1.20
elif(u>200 and u<400):
    uc=1.50
elif(u>400 and u<600):
    uc=1.80
elif(u>600):
    uc=2.00
b=u*uc
if(u>400):
    tb=b+b*0.15
else:
    tb=b+100
print(f"{tb:.2f}")