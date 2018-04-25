#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.What is the 10 001st prime number?
def prim(n):
    db=1
    for i in range(1,(n//2)+1):
        if n%i==0:
            db=db+1
    if db==2:
        return True
    return False
# print(prim(11))
def number():
    hanyadik=0
    szam=1
    while hanyadik<10001:
        if prim(szam):
            hanyadik=hanyadik+1
        szam=szam+1

print(number())
