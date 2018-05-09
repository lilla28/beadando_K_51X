#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.What is the 10 001st prime number?
def prim(n): #fv a primszamok vizsgalatara
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
# print(prim(11))
def number(): #az 10001.primszamot adja vissza
    hanyadik=0
    szam=1
    while hanyadik<10001:
        if prim(szam):
            hanyadik=hanyadik+1
        szam=szam+1
    return szam

print('a 10001-dik primszam: ',number())
