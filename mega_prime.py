def is_prime(num):
    if(num<=1):
        return False
    if(num<=3):
        return True
    if(num%2==0 or num%3==0):
        return False
    i=5
    while(i*i<=num):
        if(num%i==0 or num%(i+2)==0):
            return False
        i+=6
    return True
def is_mega_prime(number):
    for digit in str(number):
        if not is_prime(int(digit)):
            return False
    return is_prime(number)
number=int(input())
if is_mega_prime(number):
    print("Mega Prime")
else:
    print("Not Mega Prime")